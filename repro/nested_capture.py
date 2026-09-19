import io
from rich.console import Console

def scenario():
    out = io.StringIO()
    c = Console(file=out, width=20)
    c.print("BEFORE-OUTER")
    with c.capture() as outer:
        c.print("A")
        with c.capture() as inner:
            c.print("B")
        inner_result = inner.get()
        c.print("C")
    outer_result = outer.get()
    c.print("AFTER")
    return inner_result, outer_result, out.getvalue()

inner, outer, echoed = scenario()
print("expected inner == 'B\n'            actual: %r" % inner)
print("expected outer == 'A\nC\n'         actual: %r" % outer)
print("echoed (should be BEFORE-OUTER/AFTER only): %r" % echoed)
print()
# also check begin/end_capture API nesting
out2 = io.StringIO()
c2 = Console(file=out2, width=20)
c2.begin_capture()
c2.print("X")
c2.begin_capture()
c2.print("Y")
i2 = c2.end_capture()
c2.print("Z")
o2 = c2.end_capture()
print("begin/end nested: inner=%r outer=%r echo=%r" % (i2, o2, out2.getvalue()))
print()
# triple nesting
out3 = io.StringIO()
c3 = Console(file=out3, width=20)
with c3.capture() as l1:
    c3.print("1")
    with c3.capture() as l2:
        c3.print("2")
        with c3.capture() as l3:
            c3.print("3")
        r3 = l3.get()
    r2 = l2.get()
r1 = l1.get()
print("triple: l1=%r l2=%r l3=%r" % (r1, r2, r3))
