#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 07:56:31 2022

@author: paul
"""

from manim import *
from manim_physics import *
from colour import Color


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)
        square.set_fill(WHITE, opacity=1)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
        
        self.add(square)
        self.play(square.animate)
   
    
class Example(Scene):
    def construct(self):
        sq = Square(side_length=4, color= GREEN, fill_color=GREEN, fill_opacity=0.5)
        self.play(sq.animate.to_edge(LEFT), run_time=5)
        
class t(Scene):
    def construct(self):
        name = MathTex('h = {1 \over 2} g t^2')
        self.play(Create(name))
        self.play(name.animate.to_edge(UP))
        self.wait(5)
        
        
class graph(Scene):
    def construct(self):
        name = MathTex('f(x) = (e^{x \over 10} cos(x))^2 + x',fill_color=RED)
        self.play(Create(name))
        self.play(name.animate.to_edge(UP))
        self.wait(1)
                
        ax = Axes(x_range=(0,6,1), y_range=(0,10,1))
        ax_labels = ax.get_axis_labels(y_label=("f(x)"))
        func_graph = ax.plot(lambda x: (np.exp(x/10) * np.cos(x))**2 + x, x_range=(0,6,1), color=RED)
        
        graph = VGroup(ax, ax_labels)

        self.play(Create(graph))
        self.play(Create(func_graph), run_time=1)
        self.wait(5)
        
class iter_Leslie(Scene):
    def construct(self):
        name = Tex('2D Leslie Model')
        self.play(Create(name))
        self.play(name.animate.to_edge(UP))
        self.wait(1)        

        ax = Axes(x_range=(0,74,1), y_range=(0,52,1))
        ax_labels = ax.get_axis_labels()

        graph = VGroup(ax, ax_labels)

        self.play(Create(graph))
        self.wait(1)  
        
        # dots=[]
        # for i in range(100):          
        #     point = ax.coords_to_point(
        #         np.random.uniform(0,74), np.random.uniform(0,52)
        #         )
        #     dots.append(Dot(point))
        # points = VGroup(*dots)
        
        dots = [Dot(ax.coords_to_point(
            np.random.uniform(0,74), np.random.uniform(0,52)
            )) for _ in range(100)]

        points = VGroup(*dots)

        self.play(Create(points))
        self.wait(2)  

        iteration = Tex('Iteration Number:')
        self.add(iteration.to_edge(DOWN))
               
        f = 20
        param = {'lam':0.1, 'th1':f, 'th2':f, 'p1':0.7}
        
        I = 100
        for j in range(I):
            ani = [point.animate.apply_function_to_position(lambda x: ax.coords_to_point((param['th1'] * ax.point_to_coords(x)[0] + param['th2'] * ax.point_to_coords(x)[1]) * np.exp(-param['lam']*(ax.point_to_coords(x)[0] + ax.point_to_coords(x)[1])), param['p1']*ax.point_to_coords(x)[0])) for point in points]
            
            iteration_num = Tex(f'{j+1}').next_to(iteration, RIGHT)
            if j ==0 or j==1:
                self.add(iteration_num)
                self.play(*ani, run_time=1)
                self.wait()
            elif j>1 and j<5:
                self.add(iteration_num)
                self.play(*ani, run_time=1)
            elif j>=5 and j<10:
                self.add(iteration_num)
                self.play(*ani, run_time=.5)
            elif j>=10 and j<50:
                self.add(iteration_num)
                self.play(*ani, run_time=.025)
            else:
                self.add(iteration_num)
                self.play(*ani, run_time=.01)
            if j!=I-1:
                self.remove(iteration_num)

        self.wait(5)
        
        
 
class ph(Scene):
    def construct(self):
        ax = Axes(x_range=(0,74,1), y_range=(0,52,1))
        ax_labels = ax.get_axis_labels()

        graph = VGroup(ax, ax_labels)

        self.play(Create(graph))
        self.wait(1)  
        
        dots = [Dot(ax.coords_to_point(
            np.random.uniform(0,74), np.random.uniform(0,52)
            )) for _ in range(10)]

        points = VGroup(*dots)
        
        circles = [Circle(radius=1, fill_color=RED, fill_opacity=0.5).move_to(point) for point in points]
        ani = [GrowFromPoint(circle, point) for circle, point in zip(circles, points)]
        
        self.play(Create(points))
        self.wait(2) 
        self.play(*ani, run_time=2)
        self.wait(2)
        

class kmeans(Scene):
    def construct(self):
        ax = Axes(x_range=(0,74,1), y_range=(0,52,1))
        ax_labels = ax.get_axis_labels()

        graph = VGroup(ax, ax_labels)

        self.play(Create(graph))
        self.wait(1) 

        dots = [Dot(ax.coords_to_point(
            np.random.uniform(0,74), np.random.uniform(0,52)
            )) for _ in range(200)]

        
        c = [RED, BLUE, GREEN, YELLOW]
        dots2 = [Dot(ax.coords_to_point(
            np.random.uniform(0,74), np.random.uniform(0,52)
            ), color=c[i], radius=.2) for i in range(4)]


        points = VGroup(*dots)
        centeroids = VGroup(*dots2)

        f = 20
        param = {'lam':0.1, 'th1':f, 'th2':f, 'p1':0.7}
        
        for _ in range(100):
            ani = [point.apply_function_to_position(lambda x: ax.coords_to_point((param['th1'] * ax.point_to_coords(x)[0] + param['th2'] * ax.point_to_coords(x)[1]) * np.exp(-param['lam']*(ax.point_to_coords(x)[0] + ax.point_to_coords(x)[1])), param['p1']*ax.point_to_coords(x)[0])) for point in points]
        
        self.play(Create(points))
        self.wait(2) 
        self.play(Create(centeroids))
        self.wait(2)
        
        condition = False
        I=0
        for _ in range(10):
        #while not condition and I<10:
            distances = [[np.linalg.norm(point.get_center() - centeroids[0].get_center()), 
                          np.linalg.norm(point.get_center() - centeroids[1].get_center()), 
                          np.linalg.norm(point.get_center() - centeroids[2].get_center()), 
                          np.linalg.norm(point.get_center() - centeroids[3].get_center())] 
                         for point in points]
            
            shortest = np.array([distance.index(min(distance)) for distance in distances])
            
            for point, short in zip(points, shortest):
                point.set_color(c[short])
    
            self.add(points)
            self.wait(2) 
            
            centers = [VGroup(*[points[i] for i in np.argwhere(shortest==i)[:,0]]) for i in range(len(centeroids))]
            ani = [centeroid.animate.move_to(center.get_center_of_mass()) for centeroid, center in zip(centeroids, centers) if not any(np.isnan(center.get_center_of_mass()))]
    
            self.play(*ani)
            
            condition = all([all(centeroid.get_center_of_mass() - center.get_center_of_mass() < 1e-6) for centeroid, center in zip(centeroids, centers)])
            I+=1
        self.wait(2)
        
        
class numerade1(Scene):
    def construct(self):
        
        problem = VGroup(Tex('A car drives at an average velocity of 6.25 m/s.'), 
                   Tex('How far does the car travel in 4.00 s?')).arrange(DOWN)
        
        self.play(Create(problem), run_time=5)
        self.wait()
       
        num_line = NumberLine(
        x_range=[0, 25+1, 1],
        length=12,
        include_tip=True,
        include_numbers=True,
        line_to_number_buff=0.5,
    ).shift(UP)
        
        self.play(problem.animate.to_edge(UP,buff=0.5), run_time=1)
        self.play(Create(num_line), run_time=2)
        self.wait()
        
        name = Tex('Distance = (Ave. Velocity) * (Time)').next_to(num_line, DOWN, buff=1)
        self.play(Create(name))
        self.wait()

        point = Dot(num_line.number_to_point(0), radius=0.25, color=RED)
        self.play(Create(point))

        calc = MathTex('0(m) = 6.25 ({m \over s}) * 0 (s)').next_to(name, DOWN, buff=0.5)
        self.play(Create(calc))
        self.wait()          
        
        point2 = Dot(num_line.number_to_point(25), radius=0.25, color=RED)
        
        calc2 = MathTex('25(m) = 6.25 ({m \over s}) * 4 (s)').next_to(name, DOWN, buff=0.5)
        self.play(Transform(calc,calc2), Transform(point, point2), run_time=4)
        self.wait()

        final = Tex('Distance = 25 meters').next_to(name, DOWN, buff=1)
        self.play(Transform(calc, final))
        self.wait()
        
        framebox1 = SurroundingRectangle(final, buff = .25)
        self.play(
            Create(framebox1),
        )
        self.wait(5)
        
        
class logo(SpaceScene):
    def construct(self):
        circ = Circle(color=WHITE)
        v = Tex('V', color=PURE_RED, font_size=300, tex_template=TexFontTemplates.urw_zapf_chancery) #urw_zapf_chancery
        star = Star(color= PURE_BLUE, fill_color=(BLACK), fill_opacity=1)       
        logo = VGroup(circ, v, star)
        v_star = Text('V STAR').next_to(logo, DOWN, buff=1)
        self.add_sound('drum_roll.wav')        
        self.add_sound('explosion.wav', time_offset=4)

        self.play(GrowFromCenter(logo))
        self.wait()
        self.play(Create(v_star))
        self.wait()
        # self.remove(v_star)
        # self.play(logo.animate.scale(.2).to_edge(DR))
        # self.wait()
        ground = Line(LEFT * 10, RIGHT * 10, color=BLACK).to_edge(DOWN)
        self.add(ground)
        self.make_static_body(ground) 
        self.make_rigid_body(logo)
        self.make_rigid_body(v_star)
        self.wait(3)

class Density(ThreeDScene):
    def construct(self):
        wd = Text('What is Density?', color=WHITE)
        self.play(Create(wd))
        self.wait()
        self.play(wd.animate.to_edge(UP))
        
        formula1 = MathTex('Density = {Mass \over Volume}').shift(UP)
        formula2 = MathTex('\\rho = {m \over V}').next_to(formula1, DOWN, buff=1)
        self.play(Create(formula1))
        self.wait(2)
        self.play(Create(formula2))
        self.wait()
        self.wait()
        
        self.remove(wd, formula1, formula2)

        cube = Cube()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.add(cube)
        self.wait()
        
        br = Brace(cube, direction=UP)
        t = Text("length = ", font_size=25).next_to(br, RIGHT*2 + DOWN*6)
        t2 = Text("2 m", font_size=25).next_to(t, RIGHT)
        
        brace_label = VGroup(t, t2)        
        example = Text('Example: 1kg Cube').to_edge(UP)
        
        self.add(br)
        self.add_fixed_in_frame_mobjects(brace_label, example)
        self.wait(3)
        
        v = MathTex('Volume = ')
        v2 = MathTex('length^3')
        v3 = MathTex('2^3 m^3')
        v4 = MathTex('8 m^3')
        v5 = MathTex(' = {1 \over 8} {kg \over m^3}')
    
        self.add_fixed_in_frame_mobjects(formula1.to_edge(LEFT), formula2.next_to(formula1, DOWN, buff=1, aligned_edge=LEFT), v.next_to(formula2, DOWN, buff=1), v2.next_to(v, RIGHT))
        self.wait(3)        
        self.remove(v2)
        self.play(Transform(v2,v3.next_to(v, RIGHT)))
        self.wait()
        self.play(Transform(v2,v4.next_to(v, RIGHT)))
        self.wait(3)
        
        self.play(Create(v5.next_to(formula2, RIGHT)))
        self.wait()
        
        
#config.background_color = BLACK

class play(ThreeDScene):
    def construct(self):
        # circ = Circle(color=WHITE)
        # v = Tex('V', color=PURE_RED, font_size=300, tex_template=TexFontTemplates.urw_zapf_chancery) #urw_zapf_chancery
        # star = Star(color= PURE_BLUE, fill_color=(BLACK), fill_opacity=1)       
        # logo = VGroup(circ, v, star)
        # self.add_fixed_in_frame_mobjects(logo.scale(0.2).to_edge(DR))

        whatis = Text('What is Density?')
        self.play(Create(whatis))
        self.wait(3)
        self.play(whatis.animate.to_edge(UL).shift(RIGHT*2))
        self.remove(whatis)
        self.add_fixed_in_frame_mobjects(whatis.to_edge(UL).shift(RIGHT*2))

        main_formula = MathTex("Density = {mass \over Volume}")
        framebox1 = SurroundingRectangle(main_formula, buff = .25, color=PURE_RED)
        mf = VGroup(main_formula, framebox1)
        self.play(Create(main_formula))
        self.play(Create(framebox1))
        self.wait(3)

        main_formula2 = MathTex("\\rho = {m \over V}")
        framebox2 = SurroundingRectangle(main_formula2, buff = .25, color=PURE_RED)
        mf2 = VGroup(main_formula2, framebox2)

        self.play(Transform(mf, mf2))
        self.wait(3)

        self.play(mf.animate.to_edge(LEFT, buff=2))
        self.remove(mf)
        self.add_fixed_in_frame_mobjects(mf.to_edge(LEFT, buff=2))

        sphere = Sphere(fill_opacity=.5, radius = 2)
        self.set_camera_orientation(phi=65 * DEGREES, theta=90 * DEGREES)
        self.play(Create(sphere))
        self.wait(3)

        scale = ImageMobject("scale.png").rotate(PI).shift(UP*4.8+LEFT*.2)
        self.add(scale)
        self.wait(2)

        m = MathTex("mass = 4.57 g")
        v = MathTex("Volume = {4 \over 3} \\pi r^3")
        # d = MathTex("Density = {mass \over Volume}").next_to(v, DOWN, buff=1)
        d2 = MathTex("\\rho = {4.57 \over {4 \over 3} \\pi r^3} {g \over cm^3}")
        d2b = MathTex("\\rho = {4.57 \over {4 \over 3} \\pi 2^3} {g \over cm^3}")
        d2c = MathTex("\\rho = {4.57 \over {4 \over 3} \\pi 8} {g \over cm^3}")
        d2d = MathTex("\\rho = 4.57 \over {32 \over 3 \\pi} {g \over cm^3}")
        d2e = MathTex("\\rho = {(4.57)(3) \over 32 \\pi} {g \over cm^3}")
        d2f = MathTex("\\rho = {13.71 \over 100.53} {g \over cm^3}")
        d3 = MathTex("\\rho = 0.13 {g \over cm^3}")

        self.add_fixed_in_frame_mobjects(m.to_edge(UR, buff=1).shift(DOWN))
        self.wait(2)

        br1 = BraceBetweenPoints([0,0,0], [2,0,0], direction=UP)
        t1 = Text("r = 2 cm", font_size=25).next_to(br1, LEFT + DOWN*3)
        self.add(br1)
        self.add_fixed_in_frame_mobjects(t1)
        self.wait(2)

        self.add_fixed_in_frame_mobjects(v.next_to(m, DOWN, buff=1))
        self.wait(2)

        formulas = VGroup(m,v,d2)

        self.add_fixed_in_frame_mobjects(d2.next_to(v, DOWN, buff=1))
        self.wait()
        self.play(Transform(d2,d2b.next_to(v, DOWN, buff=1)))
        self.wait()
        self.play(Transform(d2,d2c.next_to(v, DOWN, buff=1)))
        self.wait()
        self.play(Transform(d2,d2d.next_to(v, DOWN, buff=1)))
        self.wait()
        self.play(Transform(d2,d2e.next_to(v, DOWN, buff=1)))
        self.wait()
        self.play(Transform(d2,d2f.next_to(v, DOWN, buff=1)))
        self.wait()
        self.play(Transform(d2,d3.next_to(v, DOWN, buff=1)))
        self.wait()
        framebox3 = SurroundingRectangle(d2)
        self.add_fixed_in_frame_mobjects(framebox3)
        self.wait(5)

        # cube = Cube()
        # self.set_camera_orientation(phi=35 * DEGREES, theta=60 * DEGREES)
        # self.add(cube)
        
        # br1 = BraceBetweenPoints([-1,1,-1], [1,1,-1], direction=UP)
        # br2 = BraceBetweenPoints([-1,1,-1], [-1,1,1])    #Line3D works
        # br3 = BraceBetweenPoints([1,-1,-1], [1,1,-1], direction=RIGHT)
        
        # braces = VGroup(br1, br2, br3)

        # t1 = Text("Length = 2 m", font_size=25).next_to(br1, UP).rotate(PI)
        # t2 = Text("Height = 2 m", font_size=25).next_to(br2).shift(LEFT)
        # t3 = Text("Width = 2 m", font_size=25).next_to(br3).rotate(PI/2).shift(LEFT)
        
        # labels = VGroup(t1, t3)
        # self.add(braces, labels)

        # v = MathTex("Volume = Length * Width * Height")
        # self.add_fixed_in_frame_mobjects(v.to_edge(UP))

        blank = Text(" ", font_size=0, color=BLACK)
        self.play(Create(blank))

class ani(Scene):
    def construct(self):
        dots = VGroup(*[Dot(color=Color(hue=j/100, saturation=1, luminance=0.5)) for j in range(100)]).arrange_in_grid(10,10)
        self.play(AnimationGroup(*[Create(d) for d in dots]))
        self.wait()

        def move_to_cent(d, t):
            radius = (1-t)*np.linalg.norm(d.get_center())
            angle = np.arctan2(d.get_y(), d.get_x()) - 2*PI*t
            d.move_to(radius*(np.cos(angle)*RIGHT + np.sin(angle)*UP))

        self.play(*[UpdateFromAlphaFunc(d, move_to_cent) for d in dots])
        self.wait()

class projectile_motion(Scene):
    def construct(self):

        table = VGroup(Line([-7,-2,0], [-5,-2,0], color=RED), Line([-5,-2,0], [-5,-4,0], color=RED), Line([-6,-2,0], [-5,-1,0], color=RED))
        self.play(Create(table))
        self.wait()

        bullet = Dot()

        def motion(bullet, t):
            v = 3
            xi = -5
            yi = -1
            T = 6
            theta = PI/4
            bullet.move_to([xi+v*np.cos(theta)*(T*t), yi+v*np.sin(theta)*(T*t)-0.49*(T*t)**2, 0])

        self.play(UpdateFromAlphaFunc(bullet, motion))
        self.wait()




