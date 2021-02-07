import matlab.engine

eng = matlab.engine.connect_matlab()
eng.sqrt(4.0)