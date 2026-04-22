import pytest


from src.plane import Plane

@pytest.fixture
def testing_plane() -> Plane:
    plane1 = Plane("e49f12",
          "PSBTL",
          "Brazil",
          -40.0644,
          -21.1308,
          876.3,
          False,
          78.09,
          348.99,
          0.65)
    return plane1

def test_equality(testing_plane):

    plane2 = Plane("e49f12",
                   "PSBTL",
                   "Brazil",
                   -40.0644,
                   -21.1308,
                   876.3,
                   False,
                   78.09,
                   348.99,
                   0.65)

    assert testing_plane == plane2

    plane3 = Plane("e49f13",
                   "PSBTL",
                   "Brazil",
                   -40.0644,
                   -21.1308,
                   876.3,
                   False,
                   78.09,
                   348.99,
                   0.65)

    assert not testing_plane == plane3

def test_equality_error(testing_plane):

    try:
        testing_plane == 'error'
    except Exception as e:
        assert TypeError == type(e)

def test_repr(testing_plane):
    assert str(testing_plane) == 'Самолет, бортовой номер: e49f12, позывной: PSBTL, страна регистрации: Brazil, координаты: (долгота: -21.1308, широта: -40.0644)'

def test_lt(testing_plane):
    plane3 = Plane("e49f13",
                   "PSBTL",
                   "Brazil",
                   -40.0644,
                   -21.1308,
                   878.3,
                   False,
                   78.09,
                   348.99,
                   0.65)

    assert testing_plane < plane3

def test_lt_false(testing_plane):
    plane3 = Plane("e49f13",
                   "PSBTL",
                   "Brazil",
                   -40.0644,
                   -21.1308,
                   871.3,
                   False,
                   78.09,
                   348.99,
                   0.65)

    assert not testing_plane < plane3

def test_lt_error(testing_plane):

    try:
        testing_plane < '2'
    except Exception as e:
        assert type(e) == TypeError

def test_le(testing_plane):
    plane3 = Plane("e49f13",
                   "PSBTL",
                   "Brazil",
                   -40.0644,
                   -21.1308,
                   871.3,
                   False,
                   78.09,
                   348.99,
                   0.65)

    assert testing_plane > plane3

def test_le_false(testing_plane):
    plane3 = Plane("e49f13",
                   "PSBTL",
                   "Brazil",
                   -40.0644,
                   -21.1308,
                   878.3,
                   False,
                   78.09,
                   348.99,
                   0.65)

    assert not testing_plane > plane3

def test_le_error(testing_plane):

    try:
        testing_plane < '2'
    except Exception as e:
        assert type(e) == TypeError

def test_plane_obj_info(testing_plane):
    assert testing_plane.plane_obj_info() == {'plane_id': "e49f12", 'call_sign': "PSBTL",'plane_country': "Brazil",
                                            'longitude': -40.0644,'latitude': -21.1308,'baro_altitude': 876.3,
                                            'on_ground': False,'velocity': 78.09,'true_track': 348.99,'vertical_rate': 0.65}