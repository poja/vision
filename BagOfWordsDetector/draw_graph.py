import matplotlib.pyplot as plt

points_all = [(0.8936170212765957, 0.7368421052631579), (0.8936170212765957, 0.7368421052631579),
              (0.9523809523809523, 0.7017543859649122), (0.9069767441860465, 0.6842105263157895),
              (0.9772727272727273, 0.7543859649122807), (0.9545454545454546, 0.7368421052631579),
              (0.9777777777777777, 0.7719298245614035), (0.9777777777777777, 0.7719298245614035),
              (0.9361702127659575, 0.7719298245614035), (0.9574468085106383, 0.7894736842105263),
              (0.975609756097561, 0.7017543859649122), (0.9555555555555556, 0.7543859649122807),
              (0.9767441860465116, 0.7368421052631579), (0.9545454545454546, 0.7368421052631579),
              (0.9736842105263158, 0.6491228070175439), (1.0, 0.6666666666666666), (0.975, 0.6842105263157895)]
points_1 = [
    (0.626984126984127, 0.9753086419753086), (0.6972477064220184, 0.9382716049382716),
    (0.5877862595419847, 0.9506172839506173), (0.5793650793650794, 0.9012345679012346),
    (0.6752136752136753, 0.9753086419753086), (0.7181818181818181, 0.9753086419753086),
    (0.6220472440944882, 0.9753086419753086), (0.6, 0.9259259259259259), (0.6982758620689655, 1.0),
    (0.7476635514018691, 0.9876543209876543), (0.6290322580645161, 0.9629629629629629),
    (0.6754385964912281, 0.9506172839506173), (0.7641509433962265, 1.0), (0.7619047619047619, 0.9876543209876543),
    (0.6779661016949152, 0.9876543209876543), (0.6991150442477876, 0.9753086419753086), (0.7043478260869566, 1.0),
    (0.7523809523809524, 0.9753086419753086), (0.7017543859649122, 0.9876543209876543),
    (0.7452830188679245, 0.9753086419753086)
]
points_2 = [(0.29850746268656714, 0.9090909090909091), (0.35294117647058826, 0.8181818181818182),
            (0.2702702702702703, 0.9090909090909091), (0.2535211267605634, 0.8181818181818182),
            (0.3333333333333333, 0.8636363636363636), (0.3541666666666667, 0.7727272727272727),
            (0.2727272727272727, 0.8181818181818182), (0.2647058823529412, 0.8181818181818182),
            (0.33962264150943394, 0.8181818181818182), (0.37209302325581395, 0.7272727272727273),
            (0.28125, 0.8181818181818182), (0.32727272727272727, 0.8181818181818182),
            (0.4186046511627907, 0.8181818181818182), (0.3902439024390244, 0.7272727272727273),
            (0.2962962962962963, 0.7272727272727273), (0.34615384615384615, 0.8181818181818182),
            (0.3584905660377358, 0.8636363636363636), (0.38095238095238093, 0.7272727272727273),
            (0.32, 0.7272727272727273), (0.38636363636363635, 0.7727272727272727)]
points_3 = [(0.21666666666666667, 0.8125), (0.2826086956521739, 0.8125), (0.20588235294117646, 0.875),
            (0.19696969696969696, 0.8125), (0.2830188679245283, 0.9375), (0.2619047619047619, 0.6875),
            (0.22580645161290322, 0.875), (0.21875, 0.875), (0.2857142857142857, 0.875), (0.325, 0.8125),
            (0.22033898305084745, 0.8125), (0.24489795918367346, 0.75), (0.375, 0.9375), (0.34210526315789475, 0.8125),
            (0.2549019607843137, 0.8125), (0.2916666666666667, 0.875), (0.30612244897959184, 0.9375),
            (0.3157894736842105, 0.75), (0.2916666666666667, 0.875), (0.34146341463414637, 0.875)]

best_points_all = [(0, 1), (0.9574468085106383, 0.7894736842105263), (0.9777777777777777, 0.7719298245614035),
                   (1.0, 0.6666666666666666), (1, 0)]
best_points_1 = [(0, 1), (0.5877862595419847, 0.9506172839506173), (0.6220472440944882, 0.9753086419753086),
                 (0.6779661016949152, 0.9876543209876543), (0.7043478260869566, 1.0), (0.7641509433962265, 1.0), (1, 0)]
best_points_2 = [(0, 1), (0.2702702702702703, 0.9090909090909091), (0.29850746268656714, 0.9090909090909091),
                 (0.3584905660377358, 0.8636363636363636), (0.4186046511627907, 0.8181818181818182), (1, 0)]
best_points_3 = [(0, 1), (0.2830188679245283, 0.9375), (0.30612244897959184, 0.9375), (0.375, 0.9375), (1, 0)]

plt.xlabel('Precision')
plt.ylabel('Recall')

x, y = [p[0] for p in points_all], [p[1] for p in points_all]
plt.scatter(x, y, c='red')
# x, y = [p[0] for p in points_1], [p[1] for p in points_1]
# plt.scatter(x, y, c='red')
# x, y = [p[0] for p in points_2], [p[1] for p in points_2]
# plt.scatter(x, y, c='green')
# x, y = [p[0] for p in points_3], [p[1] for p in points_3]
# plt.scatter(x, y, c='blue')
#
x, y = [p[0] for p in best_points_all], [p[1] for p in best_points_all]
plt.plot(x, y, 'r')
# x, y = [p[0] for p in best_points_1], [p[1] for p in best_points_1]
# plt.plot(x, y, 'r')
# x, y = [p[0] for p in best_points_2], [p[1] for p in best_points_2]
# plt.plot(x, y, 'g')
# x, y = [p[0] for p in best_points_3], [p[1] for p in best_points_3]
# plt.plot(x, y, 'b')

plt.axis([0, 1, 0, 1])
plt.grid(True)
plt.show()
