import numpy as np

# blinker
blinker1 = np.array([[0, 0, 0],
                             [0, 255, 0], 
                             [0, 255, 0], 
                             [0, 255, 0],
                             [0, 0, 0]], dtype=np.int32)
        
blinker2 = np.array([[0, 0, 0, 0, 0],
                             [0, 255, 255, 255, 0],
                             [0, 0,  0,  0,  0]], dtype=np.int32)
# toad
toad1 = np.array([[0,   0,   0,   0,   0,   0],
                             [0,   0,   0, 255,   0,   0],
                             [0, 255,   0,   0, 255,   0],
                             [0, 255,   0,   0, 255,   0],
                             [0,   0, 255,   0,   0,   0],
                             [0,   0,   0,   0,   0,   0]], dtype=np.int32)
        
toad2 = np.array([[0,   0,   0,   0,   0,   0],
                             [0,   0, 255, 255, 255,   0],
                             [0, 255, 255, 255,   0,   0],
                             [0,   0,   0,   0,   0,   0]], dtype=np.int32)
        
# beacons
beacon1 = np.array([[0,   0,   0,   0,   0,   0],
                             [0, 255, 255,   0,   0,   0],
                             [0, 255, 255,   0,   0,   0],
                             [0,   0,   0, 255, 255,   0],
                             [0,   0,   0, 255, 255,   0],
                             [0,   0,   0,   0,   0,   0]], dtype=np.int32)

beacon2 = np.array([[0,   0,   0,   0,   0,   0],
                             [0, 255, 255,   0,   0,   0],
                             [0, 255,   0,   0,   0,   0],
                             [0,   0,   0,   0, 255,   0],
                             [0,   0,   0, 255, 255,   0],
                             [0,   0,   0,   0,   0,   0]], dtype=np.int32)

# block
block = np.array([[0,   0,   0,   0],
                             [0, 255, 255,   0], 
                             [0, 255, 255,   0], 
                             [0,   0,   0,   0]], dtype=np.int32)

# b11eehive
beehive = np.array([[0,   0,   0,   0,   0,   0],
                             [0, 255,   0,   0, 255,   0],
                             [0,   0, 255,   0, 255,   0],
                             [0,   0,   0, 255,   0,   0],
                             [0,   0,   0,   0,   0,   0]], dtype=np.int32)

# loaf
loaf = np.array([[0,   0,   0,   0,   0,   0],
                 	 [0,   0, 255, 255,   0,   0],
                 	 [0, 255,   0,   0, 255,   0],
                 	 [0,   0, 255,   0, 255,   0],
                 	 [0,   0,   0, 255,   0,   0],
                 	 [0,   0,   0,   0,   0,   0]], dtype=np.int32)


# boat
boat = np.array([[0,   0,   0,   0, 0],
                        [0, 255, 255,   0, 0], 
                        [0, 255,   0, 255, 0], 
                        [0,   0, 255,   0, 0],
                        [0,   0,   0,   0, 0]], dtype=np.int32)

# tub
tub = np.array([[0,   0,   0,   0, 0],
                        [0,   0, 255,   0, 0], 
                        [0, 255,   0, 255, 0], 
                        [0,   0, 255,   0, 0],
                        [0,   0,   0,   0, 0]], dtype=np.int32)

glider1 = np.array([[0,   0,   0,   0, 0],
                        [0,   0,   0, 255, 0], 
                        [0, 255,   0, 255, 0], 
                        [0,   0, 255, 255, 0],
                        [0,   0,   0,   0, 0]], dtype=np.int32)

glider2 = np.array([[0,   0,   0,   0, 0],
                        [0, 255,   0, 255, 0], 
                        [0,   0, 255, 255, 0], 
                        [0,   0, 255,   0, 0],
                        [0,   0,   0,   0, 0]], dtype=np.int32)
        
glider3 = np.array([[0,   0,   0,   0, 0],
                        [0,   0, 255,   0, 0], 
                        [0,   0,   0, 255, 0], 
                        [0, 255, 255, 255, 0],
                        [0,   0,   0,   0, 0]], dtype=np.int32)
        
glider4 = np.array([[0,   0,   0,   0, 0],
                        [0, 255,   0,   0, 0], 
                        [0,   0, 255, 255, 0], 
                        [0, 255, 255,   0, 0],
                        [0,   0,   0,   0, 0]], dtype=np.int32)

lws1 = np.array([[0,   0,   0,   0,   0,   0,   0],
                     [0, 255,   0,   0, 255,   0,   0], 
                     [0,   0,   0,   0,   0, 255,   0], 
                     [0, 255,   0,   0,   0, 255,   0],
                     [0,   0, 255, 255, 255, 255,   0],
                     [0,   0,   0,   0,   0,   0,   0]], dtype=np.int32)
        
lws2 = np.array([[0,   0,   0,   0,   0,   0,   0],
                     [0,   0,   0, 255, 255,   0,   0], 
                     [0, 255, 255,   0, 255, 255,   0], 
                     [0, 255, 255, 255, 255,   0,   0],
                     [0,   0, 255, 255,   0,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0]], dtype=np.int32)
        
lws3 = np.array([[0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 255, 255, 255, 255,   0], 
                     [0, 255,   0,   0,   0, 255,   0], 
                     [0,   0,   0,   0,   0, 255,   0],
                     [0, 255,   0,   0, 255,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0]], dtype=np.int32)
        
lws4 = np.array([[0,   0,   0,   0,   0,   0,   0],
                     [0,   0, 255, 255,   0,   0,   0], 
                     [0, 255, 255, 255, 255,   0,   0], 
                     [0, 255, 255,   0, 255, 255,   0],
                     [0,   0,   0, 255, 255,   0,   0],
                     [0,   0,   0,   0,   0,   0,   0]], dtype=np.int32)
