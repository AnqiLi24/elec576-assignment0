"""Drive a real IPython session through a pty and save the transcript.

usage: python run_ipython.py <commands_file> <transcript_out>
Every non-blank line of <commands_file> is typed into IPython exactly as a
user would, so the transcript carries genuine In [n]: / Out[n]: prompts.
"""
import os, re, sys
import pexpect

src, out = sys.argv[1], sys.argv[2]
lines = [l for l in open(src).read().splitlines() if l.strip()]
env = {k: v for k, v in os.environ.items() if k != "VIRTUAL_ENV"}
env.update(MPLBACKEND="Agg", TERM="dumb", COLUMNS="100")
child = pexpect.spawn(
    "ipython --simple-prompt --no-banner --colors=NoColor "
    "--TerminalInteractiveShell.autoindent=False",
    encoding="utf-8", dimensions=(60, 100), env=env, timeout=120,
)
prompt = re.compile(r"In \[\d+\]: ")
child.expect(prompt)
chunks = [child.before + child.after]
for line in lines:
    child.sendline(line)
    child.expect(prompt)
    chunks.append(child.before + child.after)
child.sendline("exit")
child.expect(pexpect.EOF)
text = "".join(chunks).replace("\r\n", "\n").replace("\r", "")
text = re.sub(r"In \[\d+\]: $", "", text)          # drop trailing empty prompt
open(out, "w").write(text.rstrip() + "\n")
print(f"{out}: {text.count('In [')} inputs, {text.count('Out[')} outputs")
