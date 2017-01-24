import csv
from pathlib import Path

def length(x,y):
	return (x**2 + y**2)**0.5

def pillow_dist(x, y, alpha, beta):
	r = length(x,y)
	return (x*(1 + alpha * r**2 + beta * r**4), y*(1 + alpha * r**2 + beta * r**4))

def barrel_dist(x, y, alpha, beta):
	r = length(x,y)
	return (x/(1 + alpha * r**2 + beta * r**4), y/(1 + alpha * r**2 + beta * r**4))

def get_pillow_points(height, width, alpha, beta): 
	return [[ pillow_dist(2*x/height-1, 2*y/width-1, alpha, beta) for x in range(width+1)] for y in range(height+1)]

def get_barrel_points(height, width, alpha, beta): 
	return [[ barrel_dist(2*x/height-1, 2*y/width-1, alpha, beta) for x in range(width+1)] for y in range(height+1)]

def write_line(points, path):
	if not path.exists():
		path.touch()
	with path.open("w", newline="") as f:
		writer = csv.writer(f, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
		writer.writerows(points)

def write_files(points, root, name):
	for i in range(len(points)):
		line = points[i]
		filename = name + str(i) + ".dat"
		path = root / Path(filename)
		write_line(line, path)

if __name__ == "__main__":
	root = Path("./")
	name = "kissen"
	w = h = 5
	a = .1
	b = .1
	write_files(get_pillow_points(h, w, a, b), root, name)
	name = "tonne"
	write_files(get_barrel_points(h, w, a, b), root, name)
