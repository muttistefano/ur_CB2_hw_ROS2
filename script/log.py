import matplotlib.pyplot as plt
import numpy as np

q1 = []
q2 = []
q3 = []
q4 = []
q5 = []
q6 = []
ts = []

q1_read = []
q2_read = []
q3_read = []
q4_read = []
q5_read = []
q6_read = []
ts_read = []

f = open("inp.txt", "r")

for ln in f:
    asd = ln.split(",")
    q1.append(float(asd[0]))
    q2.append(float(asd[1]))
    q3.append(float(asd[2]))
    q4.append(float(asd[3]))
    q5.append(float(asd[4]))
    q6.append(float(asd[5]))
    ts.append(float(asd[6]))

f_out = open("out.txt", "r")

for ln in f_out:
    asd = ln.split(",")
    q1_read.append(float(asd[0]))
    q2_read.append(float(asd[1]))
    q3_read.append(float(asd[2]))
    q4_read.append(float(asd[3]))
    q5_read.append(float(asd[4]))
    q6_read.append(float(asd[5]))
    ts_read.append(float(asd[6]))

q1 = np.asarray(q1)
q2 = np.asarray(q2)
q3 = np.asarray(q3)
ts = np.asarray(ts) - ts[0]
ts = ts * 1e-6

q1_read = np.asarray(q1_read)
q2_read = np.asarray(q2_read)
q3_read = np.asarray(q3_read)
ts_read = np.asarray(ts_read) - ts_read[0]
ts_read = ts_read * 1e-6

plt.figure("q1")
plt.plot(ts,q1)
plt.plot(ts_read,q1_read)

plt.figure("q2")
plt.plot(ts,q2)
plt.plot(ts_read,q2_read)

plt.figure("q3")
plt.plot(ts,q3)
plt.plot(ts_read,q3_read)

plt.figure("q4")
plt.plot(ts,q4)
plt.plot(ts_read,q4_read)

plt.figure("q5")
plt.plot(ts,q5)
plt.plot(ts_read,q5_read)

plt.figure("q6")
plt.plot(ts,q6)
plt.plot(ts_read,q6_read)


plt.show()