import Augmentor

p = Augmentor.Pipeline("/home/workspace/snake_data/birdsnest_snakes")
# birdsnest_snakes  moonshine_snakes  starfish_snakes  yellow_snakes

p.ground_truth("/home/workspace/snake_data/birdsnest_snakes")
p.rotate(probability=1, max_left_rotation=5, max_right_rotation=5)
p.flip_left_right(probability=0.5)
p.zoom_random(probability=0.5, percentage_area=0.8)
p.flip_top_bottom(probability=0.5)
p.sample(500)


