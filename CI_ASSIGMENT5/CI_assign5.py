import random
import math
import numpy as np
import copy
cognitive_weight = 2.0
social_weight = 2.0

def objective_function(x1,x2):
    return math.sin( 2*x1-0.5*math.pi )+3*math.cos(x2)+(0.5*x1)

def velocity(velocity):
    if(velocity[0]>1):
        velocity[0]=1
    elif(velocity[0]<-0.1):
        velocity[0]=-0.1
    if(velocity[1]>1):
        velocity[1]=1
    elif(velocity[1]<-0.1):
        velocity[1]=-0.1
def position(position):
    if(position[0]>3):
        position[0]=3
    elif(position[0]< -2):
        position[0]= -2
    if(position[1]>1):
        position[1]=1
    elif(position[1]< -2):
        position[1]= -2
def pso(num_particles, num_iterations):
    particles = [{'position': np.array([random.uniform(-2, 3),random.uniform(-2, 1)]),
                  'velocity': np.array([random.uniform(-0.1, 1),random.uniform(-0.1, 1)]),
                  'personal_best': None}
                 for _ in range(num_particles)]
    
    global_best = {'position': None, 'value': 0.0}

    for i in range(num_iterations):
        for particle in particles:
            value = objective_function(particle['position'][0],particle['position'][1])
            if particle['personal_best'] is None or value > objective_function(particle['personal_best'][0],particle['personal_best'][1]):
                particle['personal_best'] = particle['position']
            if value > global_best['value']:
                global_best['value']=value
                global_best['position']= copy.deepcopy(particle['position'])
            particle['velocity'] +=  (cognitive_weight * random.uniform(0, 1) * (particle['personal_best'] - particle['position'])) + (social_weight * random.uniform(0, 1) * (global_best['position']-particle['position']))
            velocity(particle['velocity'])
            particle['position'] += particle['velocity']
            position(particle['position'])
    return global_best['position'], global_best['value']

if __name__ == '__main__':
    num_particles = 50
    num_iterations = 500
    best_position, best_value = pso(num_particles, num_iterations)
    print("best position: ", best_position)
    print("Optimal value: ",best_value)