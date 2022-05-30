from PIL import Image
import pygame
import random
import colorsys
pygame.init()

win_height = 800
win_width = 800
bg = (255,255,255)
print(bg[0])
window = pygame.display.set_mode((win_width, win_height))

filename = "dio.jpg"
img = Image.open(filename)
#img.show()
width, height = img.size

pos = []
for i in range(width):
	for j in range(height):
		pos.append((i,j))

def hsl(c):
	return colorsys.rgb_to_hsv(c[0], c[1], c[2])

def color_checker(c1,c2):
	col1 = hsl(c1)
	col2 = hsl(c2)
	if col1[0] >= col2[0]:
		return True
	else:
		return False

def dis_list(window, rect, lst):
	count = 0
	for x in range(width):
		for y in range(height):
			i,j = pos[count]
			window.set_at((rect.left + i, rect.top + j), lst[count])
			count+=1
	pygame.display.update()
	#pygame.time.delay(20)

def sel_sort(lst,rect):
	for i in range(len(lst)):
		min_idx = i
		for j in range(i+1, len(lst)):
			if lst[min_idx] > lst[j]:
				min_idx = j
		#dis_list(window,rect,lst)
		x,y = pos[i]
		x2,y2 = pos[min_idx]
		#pygame.event.pump()
		#window.set_at((rect.left + x2, rect.top + y2), lst[i])
		#window.set_at((rect.left + x, rect.top + y), lst[min_idx])
		#pygame.display.update()
		lst[i], lst[min_idx] = lst[min_idx], lst[i]

def mergeSort(a, rect):
	counter = 0
	w = 1   
	n = len(a)                                         
	while (w < n):
		l=0;
		while (l < n):
			r = min(l+(w*2-1), n-1)        
			m = min(l+w-1,n-1)          
			merge(a, l, m, r, rect, counter)
			counter += 1
			l += w*2
		w *= 2
	return a

def merge(a, l, m, r, rect, counter):
	n1 = m - l + 1
	n2 = r - m
	L = [0] * n1
	R = [0] * n2

	pygame.event.pump() 

	for i in range(0, n1):
		L[i] = a[l + i]
	for i in range(0, n2):
		R[i] = a[m + i + 1]

	i, j, k = 0, 0, l
	while i < n1 and j < n2:
		if colorsys.rgb_to_hsv(L[i][0], L[i][1], L[i][2]) >= colorsys.rgb_to_hsv(R[j][0], R[j][1], R[j][2]):
		#if L[i] >= R[j]:
			a[k] = L[i]

			x,y = pos[k]
			x2,y2 = pos[i+j]
			window.set_at((rect.left + x2, rect.top + y2), a[k])
			window.set_at((rect.left + x, rect.top + y), L[i])
			pygame.display.update()

			i += 1
		else:
			a[k] = R[j]
			
			x,y = pos[k]
			x2,y2 = pos[j+i]
			window.set_at((rect.left + x2, rect.top + y2), a[k])
			window.set_at((rect.left + x, rect.top + y), R[j])
			pygame.display.update()

			j += 1
		pygame.time.delay(1)
		k += 1

	while i < n1:
		a[k] = L[i]

		x,y = pos[k]
		x2,y2 = pos[i+j]
		window.set_at((rect.left + x2, rect.top + y2), a[k])
		window.set_at((rect.left + x, rect.top + y), L[i])
		pygame.display.update()
		pygame.time.delay(1)

		i += 1
		k += 1

	while j < n2:
		a[k] = R[j]

		x,y = pos[k]
		x2,y2 = pos[j+i]
		window.set_at((rect.left + x2, rect.top + y2), a[k])
		window.set_at((rect.left + x, rect.top + y), R[j])
		pygame.display.update()
		pygame.time.delay(1)

		j += 1
		k += 1
	
	
def bubble_sort(window, rect, lst):
	print("h")
	c = 0
	for i in range(len(lst)-1):
		for j in range(len(lst)-1-i):

			if lst[j] > lst[j+1]:
				print(c)
				c+=1
				x,y = pos[j]
				x2,y2 = pos[j+1]
				window.set_at((rect.left + x2, rect.top + y2), lst[j])
				window.set_at((rect.left + x, rect.top + y), lst[j+1])
				pygame.display.update()
				#dis_list(window,rect,lst)
				t = lst[j]
				lst[j] = lst[j+1]
				lst[j+1] = t


def get_pixels(width, height, lst):
	lst = []
	for i in range(width):
		for j in range(height):
			colors = img.getpixel((i,j))
			lst.append( colors)
	print(len(lst))
	return lst

def main():
	run = True
	clock = pygame.time.Clock()

	color =img.getpixel((1,1))
	lst = []
	lst = get_pixels(width,height,lst)


	pygame.display.set_caption("sort")
	window.fill(bg)
	pygame.display.update()
	
	rect = pygame.Rect(0, 0, width, height)
	rect.centerx = win_width//2
	rect.centery = win_height//2
	dis_list(window,rect,lst)
	
	while run:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type != pygame.KEYDOWN:
				continue
			if event.key == pygame.K_r:
				lst = get_pixels(width,height,lst)
				dis_list(window,rect,lst)
			if event.key == pygame.K_k:
				lst.sort()
				dis_list(window,rect,lst)
			elif event.key == pygame.K_j:
				dis_list(window,rect,lst)
			elif event.key == pygame.K_SPACE:
				#lst.sort() #low key kinda cool
				#sel_sort(lst,rect)
				#countingSort(lst)
				mergeSort(lst, rect)
				print("EHBWIEWHN")
				pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()
