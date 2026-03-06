FROM python:3.9-slim

WORKDIR /app

WORKDIR ../LR1/geometric_lib

RUN echo '#!/usr/bin/env python3\n\
import sys\n\
sys.path.append("/app/geometric_lib")\n\
from circle import area as circle_area\n\
from square import area as square_area\n\
\n\
def main():\n\
    # Чтение из файла через volume\n\
    with open("/data/input.txt", "r") as f:\n\
        shape, value = f.read().strip().split()\n\
    \n\
    value = float(value)\n\
    \n\
    if shape == "circle":\n\
        result = circle_area(value)\n\
    elif shape == "square":\n\
        result = square_area(value)\n\
    else:\n\
        result = "Unknown shape"\n\
    \n\
    with open("/data/output.txt", "w") as f:\n\
        f.write(str(result))\n\
\n\
if __name__ == "__main__":\n\
    main()' > calculate.py

RUN chmod +x calculate.py

CMD ["python3", "calculate.py"]

