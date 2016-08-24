from peak_trough_detection import find_min

def test_find_min_all_small_positive():
	assert find_min([0.01, 0.01, 0.02, 0.015, 0.005], 0.1) ==  4, "Should return 4"

def test_find_min_1_small_negative():
	assert find_min([0.01, -0.01, 0.02, 0.015, 0.005], 0.1) ==  1, "Should return 1"	