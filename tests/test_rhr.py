from lithomap.rhr import dip_direction_azimuth, strike_rhr

def test_cardinal_azimuths():
    assert dip_direction_azimuth("N") == 0
    assert dip_direction_azimuth("E") == 90
    assert dip_direction_azimuth("S") == 180
    assert dip_direction_azimuth("W") == 270

def test_rhr_preserves_or_flips_strike():
    assert strike_rhr(0, "E") == 0
    assert strike_rhr(0, "W") == 180
