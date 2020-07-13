import morseCode

def test_preklad_zpravy_probehl_v_poradku():
    vysledek = morseCode.toMorse('Test překladu')
    assert vysledek == '-/*/***/-/*--*/*-*/*/-*-/*-**/*-/-**/**-'
