#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 07:56:31 2022

@author: paul
"""

from manim import *
from manim_physics import *
from colour import Color


class iter_Leslie(Scene):
    def construct(self):
        name = Tex('2D Leslie Model')
        self.play(Create(name))
        self.play(name.animate.to_edge(UP))
        self.wait(1)

        ax = Axes(x_range=(0, 74, 1), y_range=(0, 52, 1))
        ax_labels = ax.get_axis_labels()

        graph = VGroup(ax, ax_labels)

        self.play(Create(graph))
        self.wait(1)
        dots = [Dot(ax.coords_to_point(
            np.random.uniform(0, 74), np.random.uniform(0, 52)
        )) for _ in range(100)]

        points = VGroup(*dots)

        self.play(Create(points))
        self.wait(2)

        iteration = Tex('Iteration Number:')
        self.add(iteration.to_edge(DOWN))

        f = 20
        param = {'lam': 0.1, 'th1': f, 'th2': f, 'p1': 0.7}

        animates = []
        I = 100
        for j in range(I):

            ani = [point.animate.apply_function_to_position(
                lambda x: ax.coords_to_point(
                    (param['th1'] * ax.point_to_coords(x)[0] +
                     param['th2'] * ax.point_to_coords(x)[1])
                    * np.exp(-param['lam']*(ax.point_to_coords(x)
                             [0] + ax.point_to_coords(x)[1])),
                    param['p1']*ax.point_to_coords(x)[0])
            ) for point in points]

            iteration_num = Tex(f'{j+1}').next_to(iteration, RIGHT)
            self.add(iteration_num)
            self.play(*ani, run_time=np.exp(-j/10))
            if j != I-1:
                self.remove(iteration_num)
        self.wait(5)


class kmeans(Scene):
    def construct(self):
        ax = Axes(x_range=(0, 74, 1), y_range=(0, 52, 1))
        ax_labels = ax.get_axis_labels()

        graph = VGroup(ax, ax_labels)

        self.play(Create(graph))
        self.wait(1)

        dots = [Dot(ax.coords_to_point(
            np.random.uniform(0, 74), np.random.uniform(0, 52)
        )) for _ in range(500)]

        c = [RED, BLUE, GREEN, YELLOW]
        dots2 = [Dot(ax.coords_to_point(
            np.random.uniform(0, 74), np.random.uniform(0, 52)
        ), color=c[i], radius=.2) for i in range(4)]

        points = VGroup(*dots)
        centeroids = VGroup(*dots2)

        f = 20
        param = {'lam': 0.1, 'th1': f, 'th2': f, 'p1': 0.7}

        for _ in range(100):
            ani = [point.animate.apply_function_to_position(
                lambda x: ax.coords_to_point(
                    (param['th1'] * ax.point_to_coords(x)[0] +
                     param['th2'] * ax.point_to_coords(x)[1])
                    * np.exp(-param['lam']*(ax.point_to_coords(x)
                             [0] + ax.point_to_coords(x)[1])),
                    param['p1']*ax.point_to_coords(x)[0])
            ) for point in points]

        self.play(Create(points))
        self.wait(2)
        self.play(Create(centeroids))
        self.wait(2)

        for _ in range(10):
            distances = [[np.linalg.norm(point.get_center() - centeroids[0].get_center()),
                          np.linalg.norm(point.get_center() -
                                         centeroids[1].get_center()),
                          np.linalg.norm(point.get_center() -
                                         centeroids[2].get_center()),
                          np.linalg.norm(point.get_center() - centeroids[3].get_center())]
                         for point in points]

            shortest = np.array([distance.index(min(distance))
                                for distance in distances])

            for point, short in zip(points, shortest):
                point.set_color(c[short])

            self.add(points)
            self.wait(2)

            centers = [VGroup(
                *[points[i] for i in np.argwhere(shortest == i)[:, 0]]
            ) for i in range(len(centeroids))]

            ani = [centeroid.animate.move_to(
                center.get_center_of_mass()
            ) for centeroid, center in zip(centeroids, centers)
                if not any(np.isnan(center.get_center_of_mass()))]

            self.play(*ani)

        self.wait(2)
