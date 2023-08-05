#pylint: disable=wrong-import-position,wrong-import-order,superfluous-parens
import os
import argparse
import sys
import traceback
import errno
import json
import tqdm
import dxf
import dxf.exceptions
import requests.exceptions

_choices = ['auth',
            'push-blob',
            'pull-blob',
            'blob-size',
            'mount-blob',
            'del-blob',
            'set-alias',
            'get-alias',
            'del-alias',
            'get-digest',
            'get-manifest',
            'list-aliases',
            'list-repos']

_parser = argparse.ArgumentParser()
_subparsers = _parser.add_subparsers(dest='op')
for c in _choices:
    sp = _subparsers.add_parser(c)
    if c != 'list-repos':
        sp.add_argument("repo")
        sp.add_argument('args', nargs='*')

def _flatten(l):
    r = []
    for sublist in l:
        if isinstance(sublist, dict):
            r.append(sublist)
        else:
            for item in sublist:
                r.append(item)
    return r

# pylint: disable=too-many-statements
def doit(args, environ):
    dxf_progress = environ.get('DXF_PROGRESS')
    progress = None
    if dxf_progress == '1' or (dxf_progress != '0' and sys.stderr.isatty()):
        bars = {}
        def do_progress(dgst, chunk, size):
            if dgst not in bars:
                bars[dgst] = tqdm.tqdm(desc=dgst[0:8],
                                       total=size,
                                       leave=True)
            if chunk:
                bars[dgst].update(len(chunk))
            if bars[dgst].n >= bars[dgst].total:
                bars[dgst].close()
                del bars[dgst]
        progress = do_progress

    dxf_skiptlsverify = environ.get('DXF_SKIPTLSVERIFY')
    if dxf_skiptlsverify == '1':
        dxf_tlsverify = False
    else:
        dxf_tlsverify = environ.get('DXF_TLSVERIFY', True)

    def auth(dxf_obj, response):
        # pylint: disable=redefined-outer-name
        username = environ.get('DXF_USERNAME')
        password = environ.get('DXF_PASSWORD')
        authorization = environ.get('DXF_AUTHORIZATION')
        dxf_obj.authenticate(username, password,
                             response=response,
                             authorization=authorization)

    args = _parser.parse_args(args)
    if args.op != 'list-repos':
        dxf_obj = dxf.DXF(environ['DXF_HOST'],
                          args.repo,
                          auth,
                          environ.get('DXF_INSECURE') == '1',
                          environ.get('DXF_AUTH_HOST'),
                          tlsverify=dxf_tlsverify)
    else:
        dxf_obj = dxf.DXFBase(environ['DXF_HOST'],
                              auth,
                              environ.get('DXF_INSECURE') == '1',
                              environ.get('DXF_AUTH_HOST'),
                              tlsverify=dxf_tlsverify)

    def _doit():
        # pylint: disable=too-many-branches,too-many-locals
        if args.op == "auth":
            username = environ.get('DXF_USERNAME')
            password = environ.get('DXF_PASSWORD')
            authorization = environ.get('DXF_AUTHORIZATION')
            token = dxf_obj.authenticate(username, password,
                                         actions=args.args,
                                         authorization=authorization)
            if token:
                print(token)
            return

        token = environ.get('DXF_TOKEN')
        if token:
            dxf_obj.token = token

        if args.op == "push-blob":
            if len(args.args) < 1:
                _parser.error('too few arguments')
            if len(args.args) > 2:
                _parser.error('too many arguments')
            if len(args.args) == 2 and not args.args[1].startswith('@'):
                _parser.error('invalid alias')
            dgst = dxf_obj.push_blob(args.args[0], progress)
            if len(args.args) == 2:
                dxf_obj.set_alias(args.args[1][1:], dgst)
            print(dgst)

        elif args.op == "pull-blob":
            _stdout = getattr(sys.stdout, 'buffer', sys.stdout)
            platform = environ.get('DXF_PLATFORM')
            if args.args:
                dgsts = _flatten([dxf_obj.get_alias(name[1:], platform=platform)
                                  if name.startswith('@') else [name]
                                  for name in args.args])
            else:
                dgsts = _flatten([dxf_obj.get_alias(manifest=sys.stdin.read())])
            for dgst in dgsts:
                if isinstance(dgst, dict):
                    print(json.dumps(dgst, sort_keys=True))
                    continue
                it, size = dxf_obj.pull_blob(
                    dgst, size=True, chunk_size=environ.get('DXF_CHUNK_SIZE'))
                if environ.get('DXF_BLOB_INFO') == '1':
                    print(dgst + ' ' + str(size))
                if progress:
                    progress(dgst, b'', size)
                for chunk in it:
                    if progress:
                        progress(dgst, chunk, size)
                    _stdout.write(chunk)

        elif args.op == 'blob-size':
            platform = environ.get('DXF_PLATFORM')
            if args.args:
                sizes = [dxf_obj.get_alias(name[1:],
                                           sizes=True,
                                           platform=platform)
                         if name.startswith('@') else
                         [(name, dxf_obj.blob_size(name))]
                         for name in args.args]
            else:
                sizes = [dxf_obj.get_alias(manifest=sys.stdin.read(),
                                           sizes=True,
                                           platform=platform)]
            for tuples in sizes:
                if isinstance(tuples, dict):
                    print(json.dumps({
                        key: sum(size for _, size in value)
                        for key, value in tuples.items()
                    }, sort_keys=True))
                else:
                    print(sum(size for _, size in tuples))

        elif args.op == 'mount-blob':
            if len(args.args) < 2:
                _parser.error('too few arguments')
            if len(args.args) > 3:
                _parser.error('too many arguments')
            if len(args.args) == 3 and not args.args[2].startswith('@'):
                _parser.error('invalid alias')
            dgst = dxf_obj.mount_blob(args.args[0], args.args[1])
            if len(args.args) == 3:
                dxf_obj.set_alias(args.args[2][1:], dgst)
            print(dgst)

        elif args.op == 'del-blob':
            if args.args:
                dgsts = _flatten([dxf_obj.del_alias(name[1:])
                                  if name.startswith('@') else [name]
                                  for name in args.args])
            else:
                dgsts = _flatten([dxf_obj.get_alias(manifest=sys.stdin.read())])
            for dgst in dgsts:
                if isinstance(dgst, dict):
                    for v in dgst.values():
                        for d in dxf_obj.del_alias(v):
                            dxf_obj.del_blob(d)
                else:
                    dxf_obj.del_blob(dgst)

        elif args.op == "set-alias":
            if len(args.args) < 2:
                _parser.error('too few arguments')
            dgsts = [dxf.hash_file(dgst) if os.sep in dgst else dgst
                     for dgst in args.args[1:]]
            sys.stdout.write(dxf_obj.set_alias(args.args[0], *dgsts))

        elif args.op == "get-alias":
            platform = environ.get('DXF_PLATFORM')
            if args.args:
                dgsts = _flatten([dxf_obj.get_alias(name, platform=platform)
                                 for name in args.args])
            else:
                dgsts = _flatten([dxf_obj.get_alias(manifest=sys.stdin.read(),
                                                    platform=platform)])
            for dgst in dgsts:
                print(json.dumps(dgst, sort_keys=True) if isinstance(dgst, dict) else dgst)

        elif args.op == "del-alias":
            dgsts = _flatten([dxf_obj.del_alias(name) for name in args.args])
            for dgst in dgsts:
                print(json.dumps(dgst, sort_keys=True) if isinstance(dgst, dict) else dgst)

        elif args.op == 'get-digest':
            platform = environ.get('DXF_PLATFORM')
            if args.args:
                dgsts = [dxf_obj.get_digest(name, platform=platform)
                         for name in args.args]
            else:
                dgsts = [dxf_obj.get_digest(manifest=sys.stdin.read(),
                                            platform=platform)]
            for dgst in dgsts:
                print(json.dumps(dgst, sort_keys=True) if isinstance(dgst, dict) else dgst)

        elif args.op == 'get-manifest':
            platform = environ.get('DXF_PLATFORM')
            for name in args.args:
                manifest = dxf_obj.get_manifest(name, platform=platform)
                sys.stdout.write(json.dumps(manifest, sort_keys=True) if isinstance(manifest, dict) else manifest)

        elif args.op == 'list-aliases':
            if args.args:
                _parser.error('too many arguments')
            for name in dxf_obj.list_aliases(iterate=True):
                print(name)

        elif args.op == 'list-repos':
            for name in dxf_obj.list_repos(iterate=True):
                print(name)

    try:
        _doit()
        return 0
    except dxf.exceptions.DXFUnauthorizedError:
        traceback.print_exc()
        return errno.EACCES
    except requests.exceptions.HTTPError as ex:
        # pylint: disable=no-member
        if ex.response.status_code == requests.codes.not_found:
            traceback.print_exc()
            return errno.ENOENT
        raise

def main():
    sys.exit(doit(sys.argv[1:], os.environ))
