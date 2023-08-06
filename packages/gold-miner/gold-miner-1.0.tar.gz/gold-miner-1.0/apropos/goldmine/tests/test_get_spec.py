from io import StringIO
import yaml


def test_get_spec():
    spec = """---
globalitem: foo
test:
  testspec: one
  override: two
  tests:
    - file: bogus
      override: three
    - file: other
      testspec: four
"""

    from apropos.goldmine.tools.tande import TestAndEval

    c = TestAndEval()

    plan = yaml.safe_load(spec)
    assert plan["test"]["tests"][0]["file"] == "bogus"  # ensure data load

    assert (
        c.get_spec(plan, plan["test"]["tests"][0], "dne", default="usedefault")
        == "usedefault"
    )

    assert (
        c.get_spec(plan, plan["test"]["tests"][0], "override", default="usedefault")
        == "three"
    )

    assert (
        c.get_spec(
            plan,
            plan["test"]["tests"][1],
            "testspec",
            paths=["test"],
            default="usedefault",
        )
        == "four"
    )

    assert (
        c.get_spec(
            plan,
            plan["test"]["tests"][0],
            "override",
            paths=["test"],
            default="usedefault",
        )
        == "three"
    )

    assert (
        c.get_spec(
            plan,
            plan["test"]["tests"][0],
            "testspec",
            paths=["test"],
            default="usedefault",
        )
        == "one"
    )

    # accept non-lists for simple cases
    assert (
        c.get_spec(
            plan,
            plan["test"]["tests"][0],
            "testspec",
            paths="test",
            default="usedefault",
        )
        == "one"
    )

    assert (
        c.get_spec(
            plan,
            plan["test"]["tests"][0],
            "globalitem",
            paths=["test"],
            default="usedefault",
        )
        == "foo"
    )

    assert (
        c.get_spec(
            plan,
            plan["test"]["tests"][0],
            "nosuch",
            paths=["test"],
            default="usedefault",
        )
        == "usedefault"
    )
