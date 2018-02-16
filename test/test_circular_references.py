import pytest  # noqa
import python_jsonschema_objects as pjo


def test_circular_references(markdown_examples):

    builder = pjo.ObjectBuilder(markdown_examples['Circular References'])
    klasses = builder.build_classes()
    a = klasses.A()
    a1 = klasses.A()
    b = klasses.B()
    a.message = 'foo'
    a1.message = 'bar'
    b.author = "James Dean"
    a.reference = b
    a.others = [a1]

    assert a.reference == b
    assert a.others[0] == a1
    assert b.oreference == None  # noqa
    assert a.message == "foo"

    serialized = a.serialize(sort_keys=True)
    assert serialized == '{"message": "foo", "others": [{"message": "bar"}], "reference": {"author": "James Dean"}}'  # noqa
    
