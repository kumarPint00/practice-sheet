#program to multiply two matrix
X=[[1,2,3],[3,5,4],[9,0,1]]
Y=[[1,2,3],[3,5,4],[9,0,1]]

result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
  for j in range(len(Y[0])):
    for k in range(len(Y)):
      result[i][j]+=X[i][k]+Y[k][j]


for r in result:
  print(r)

  
