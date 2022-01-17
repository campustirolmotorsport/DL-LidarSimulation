from src.world.field import Field

size = (500, 500)
space = ((0, 5), (0, 5), 0.01)


def test_getPixel():
    field = Field(size, space)
    assert (0, 0) == field.getPixel((0, 0))
