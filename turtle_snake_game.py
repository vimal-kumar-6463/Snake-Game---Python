from turtle import Turtle , Screen 
import time
import random 

class SnakeGame :
    
    def __init__(self):
        self.S = Screen()
        self.S.setup(height = 600 , width = 600)
        self.S.tracer(0)
        self.S.bgcolor('black')
        self.starting_pos = [(0,0),(-20,0),(-40,0),(-60,0)]
        self.segments = []
        self.food = None
        self.display = Turtle()
        self.display.color("yellow")
        self.display.penup()
        self.display.goto(0,270)
        self.display.pendown()
        self.game_status = True
        self.score = 0
        for i in range(4):
            T = Turtle(shape = 'square')
            T.color('white')
            T.penup()
            self.segments.append(T)
            T.goto(self.starting_pos[i][0],self.starting_pos[i][1])   
        self.S.update()   
        self.segments.reverse() 
        self.head = self.segments[-1]
        self.food = Turtle(shape="circle")
        self.food.color('blue')
        self.food.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.food.penup()
        self.food.goto(random.randint(-270,270),random.randint(-270,270))
    
    def level_up(self) :
        self.level += 1
        return True

            
    def set_listener(self):
        self.S.listen()
        self.S.onkey(key="Right" , fun = self.turn_right)
        self.S.onkey(key="Left" , fun = self.turn_left)
        self.S.onkey(key="g" , fun = self.grow)
        self.S.onkey(key="p" , fun = self.place_food)
        
            
    def turn_left(self) :
        self.head.left(90)
        return True
    
    def dist_btw(self,t1,t2) :
        return ((t1.pos()[0]-t2.pos()[0])**2)+((t1.pos()[1]-t2.pos()[1])**2)**1/2
    
    def is_food(self):
        if self.dist_btw(self.head,self.food) < 60:
            self.score += 1
            self.grow()
            self.place_food()
            return True
        return False
    
    def turn_right(self):
        self.head.right(90)
        return True
    
    def place_food(self):
        self.food.goto(random.randint(-270,270),random.randint(-270,270))
        return True
    
    def is_out_of_boundary(self):
        position = self.head.pos()
        if position[0] >= 300 or position[0] <= -300 or position[1] >= 300 or position[1] <= -300 :
            self.game_status = False
            print(f"you have lost and your score is {self.score}")
            self.S.bye()
        
    def is_collided(self):
        for i in range(0,len(self.segments)-4):
            if self.dist_btw(self.head , self.segments[i]) < 25 :
                self.game_status = False
                print(f"you have lost and your score is {self.score}")
                self.S.bye()
                
    def grow(self):
        T = Turtle(shape = 'square')
        T.color('white')
        T.penup()
        self.segments.insert(0,T)
        
    def move(self) :
        
        while True :
            self.S.update()
            for i in range(0,len(self.segments)-1) :
                self.segments[i].goto(self.segments[i+1].pos()[0],self.segments[i+1].pos()[1]) 
        
            self.head.forward(10)
            time.sleep(0.06)    
            self.is_food()
            self.is_collided()
            self.display.clear()
            self.display.write(arg = f"Score : {self.score}",align="center",font=('impact',20))
            self.display.hideturtle()
            self.is_out_of_boundary()
            
            
                  
                  


game = SnakeGame()
game.set_listener()
game.move()                





    













game.S.exitonclick()