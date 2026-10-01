"""Fill the design agent's templates/CLAUDE.md from a manifest.

Usage: python3 fill_claude_md.py <agent-repo>/templates/CLAUDE.md design-system-manifest.yaml > fuji.md
Simple {{a.b.c}} placeholders are looked up in the manifest; the descriptive ones
(styles, roles, radius, components, brandGuidelines) are formatted below. Any
placeholder it can't fill is left as-is and reported on stderr.
"""
import re, sys, yaml

tpl, man = open(sys.argv[1]).read(), yaml.safe_load(open(sys.argv[2]))

def get(path):
    v = man
    for k in path.split('.'):
        v = v[k]
    return v

def fmt(v):
    if isinstance(v, dict):
        return ', '.join(f'{k} {x}' for k, x in v.items())
    if isinstance(v, list):
        return '; '.join(map(str, v))
    return str(v)

def special(key):
    k = key.split(' ')[0].split('—')[0].strip()
    if k == 'typography.styles':
        return '; '.join(f"{s['name']} {s['step']}/{s['weight']}" for s in man['typography']['styles'])
    if k == 'spacing.roles':
        return '; '.join(f"{r['name']} {r['px']}" + (f" ({', '.join(r['appliesTo'])})" if r.get('appliesTo') else '') for r in man['spacing']['roles'])
    if k == 'radius.tokens':
        return ', '.join(f"{r['name']} {r['px']}" for r in man['radius']['tokens'])
    if key.startswith('approved components'):
        out = []
        for c in man['components']:
            v = [x['name'] for x in c.get('variants', []) if x.get('status') == 'approved']
            s = c['name'] + (f" ({'/'.join(v)})" if v else '')
            if c.get('status') != 'approved':
                s += " — pending, don't reuse"
            out.append(s)
        return '; '.join(out)
    if k == 'brandGuidelines':
        out = []
        for b in man.get('brandGuidelines', []):
            prof = yaml.safe_load(open(b['profile'])) if b.get('profile') else {}
            name = prof.get('name', b['profile'])
            if b.get('applies') == 'always':
                out.append(f"{name} (`{b['profile']}`): this product's own")
            else:
                ds = b.get('designSystem', '').replace('design-system-manifest.yaml', 'CLAUDE.md')
                out.append(f'{name} (`{b["profile"]}`): a reference, used only when declared (`brandGuidelines: ["{name}"]` in the brief or page); its system is `{ds}`')
        return '; '.join(out) or 'none'
    return get(k)

def repl(m):
    key = m.group(1).strip()
    try:
        return fmt(special(key))
    except Exception:
        print(f'unfilled: {key}', file=sys.stderr)
        return m.group(0)

print(re.sub(r'\{\{(.+?)\}\}', repl, tpl), end='')
