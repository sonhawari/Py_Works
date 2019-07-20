

5+5

1/2

2^6

1 == 2

1 ~= 2

1 && 0 

xor(1,0)

a= 3

a = pi;

disp(a)

disp(sprintf('2 decimals: %0.2f', a))

A = [1 2; 3 4; 5 6]

V = [ 1 2 3]

V = [1; 2; 3]



v = 1:0.1:2

v = 1:6

ones(2,3)

C = 2*ones(2,3)

W = ones(1,3)

W = zeros(1,3)



W = rand(1,3)


rand(3,3)

W rand(1,3)


W = -6 + sqrt(10) * (randn(1,10000))
hist(w)
hist(w,50)



eye(4)

eye(6)

help eye

help rand

----------------------

A = [1 2; 3 4; 5 6]

sizeA = size(A)

size(A,1)
size (A,2)

v = [1 2 3 4]
l = length(v)

disp(length(A))

pwd

cd 'C:\Users'

pwd

ls


cd 'C:\Users\eiree\Documents\GitHub\Py_Works\Coursera_Machine_Learning\Octave'


pwd
ls



load featuresX.dat
load priceY.dat

load('featuresX.dat')
load('priceY.dat')





featuresX

size(featuresX)


size(priceY)



whos



clear featuresX

whos


v = priceY(1:10)

save hello.mat v;

clear

load hello.mat


save hello.txt v -ascii


A = [1 2; 3 4; 5 6 ]


A(3,2)

A(2, :)


A(:, 2)


A([1 3], :)



A(:,2)

A(:, 2) = [10 ; 11; 12]



A = [A, [100; 101; 102]]


size(A)

A(:) % put all elements of A into a single vector

A = [1 2; 3 4; 5 6 ]
B = [11 12; 13 14; 15 16]


C = [A B]


C = [A ; B]



t = [0:0.01:0.98]

t

y1 = sin(2*pi*4*t)
plot(t,y1)

y2 = cos(2*pi*4*t)
plot(t,y2)

plot(t,y1)
hold on
plot(t,y2,'r')
xlabel('time')
ylabel('value')

legend('sin','cos')
title('my plot')


print -dpng 'myplot.png'

help plot

close

figure(1); plot(t,y1)
figure(2); plot(t,y2)


subplot(1,2,1)
plot(t,y1)
subplot(1,2,2)
plot(t,y2)


axis([0.5 1 -1 1])

subplot(1,2,1)
axis([0.5 1 -1 1])



clf



A = magic(5)


imagesc(A)


imagesc(A), colorbar , colormap gray



A = magic(15)
imagesc(A), colorbar , colormap gray


a=1 , b=2, c=3

a=1;  b=2; c=3;



v = zeros(10 , 1)
v


for i = 1:10,
  v(i) = 2^i;
  end;

v


indices = 1:10;
indices


for i = indices,
  disp(i);
  end;


i = 1;
while i <= 5,
  v(i) = 100;
  i = i+1;
  end;


i = 1;
while true,
  v(i) = 999;
  i = i+1;
  if i == 6,
    break;
  end;
end;



v(1)

v(1) = 2;
if v(1) ==1,
  disp('a')
elseif v(1) ==2,
  disp('b')
else
  disp('c')
end;

SquareThisFunc

SquareThisFunc(10)


% Octave search path
addpath('C:/Users/eiree/Documents/GitHub/Py_Works/Coursera_Machine_Learning/Octave')


squareAndcube(2)







x = [1 1; 1 2; 1 3]

y = [1 ; 2; 3]

theta = [0;1]
addpath('C:/Users/eiree/Documents/GitHub/Py_Works/Coursera_Machine_Learning/Octave')


costFunctionJ(x,y, theta)



theta = [0;0]
costFunctionJ(x,y, theta)















