import scipy.io 
import numpy as np

def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1
 
def quick_sort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quick_sort(array, low, pi - 1)
    quick_sort(array, pi + 1, high)

def sortIndex(lst):
  index = []
  for i in lst:
    temp = 0
    for j in i:
      if j.isdecimal() :
        index.append(int(i[temp:]))
        break
      else:
        temp += 1
  code = lst[0][:temp]
  quick_sort(index,0,len(index)-1)
  for i in range (0,len(index)):
    index[i] = code+str(index[i])
  return index

# sort dictionary by values
def sortDictByVal(his,rev):
  sorted_dict = {}
  sorted_keys = sorted(his, key=his.get, reverse= rev)
  for w in sorted_keys:
      sorted_dict[w] = his[w]
  return sorted_dict

def sortDictByKey(his):
  temp = {}
  key = list(his.keys())
  key = sortIndex(key)
  for i in key:
    temp[i] = his[i]
  return temp

# generate user transactions
def user_total_trans(transactions, history):
  his = {}
  trans = {}
  user = {}
  for i in history:
    his.update({i[0][0]: [str(np.char.strip(e)) for e in i[1]]})
  # Ex: his = {'U1': ['T100', 'T400'], 'U2': ['T200', 'T300', 'T700'], ...}

  for i in transactions:
    trans.update({i[0][0]: [e.strip() for e in i[1]]})
  # Ex: trans = {'T100': ['I1', 'I2', 'I5'], 'T200': ['I2', 'I4'],...}

  for i in his:
    temp = {}
    for tran in his[i]:
      for id in trans[tran]:
        try:
          temp.update({id: temp[id]+1})    
        except:
          temp[id] = 1
    user.update({i: temp})
  # Ex: res = {'U1': {'I1': 2, 'I2': 2, 'I4': 1, 'I5': 1},'U2': {'I1': 1, 'I2': 2, 'I3': 2, 'I4': 1},...}
  return user

# best-seller products
def req1(transactions):    
  res = {}
  # res = {ID: numbers of product}
  vmin = []
  vmax = []
  # Ex: i->[['T100'],['I1', 'I2', 'I5']], j -> ['I1', 'I2', 'I5']
  for i in transactions: 
    for j in i[1]:
        try:
          res.update({j: res[j]+1})    
        except:
          res[j] = 1
  # Ex: res = {'I1': 7, 'I2': 8, 'I5': 2, 'I4': 2, 'I3': 7}

  rmax = res[max(res, key=res.get)]
  rmin = res[min(res, key=res.get)]
  # add min, max -> vmax, vmin
  for i in res:
    if res[i] == rmax:
      vmax.append(i)
    if res[i] == rmin:
      vmin.append(i)
  # sort result
  vmin = sortIndex(vmin)
  vmax = sortIndex(vmax)
  return vmax,vmin

def req2(products):
  inve = []
  vmax = []
  vmin = []
  # i: inventory
  # products: ['I1', '10', '5', '1']
  for i in products:
    inve.append(int(i[2]))
  # Ex: inve = [5, 2, 10, 0, 10, 4]

  # append product -> list
  for i in products:
    if int(i[2]) == max(inve):
      vmax.append(i[0].strip())
    if int(i[2]) == min(inve):
      vmin.append(i[0].strip())
  vmin = sortIndex(vmin)
  vmax = sortIndex(vmax)
  return vmax,vmin

def req3(transactions, products):
  q = {}
  p = {}
  #get numbers of products
  for i in transactions:
    for j in i[1]:
        try:
          q.update({j: q[j]+1})    
        except:
          q[j] = 1
  # Ex: q = {'I1': 7, 'I2': 8, 'I5': 2, 'I4': 2, 'I3': 7}

  #get price of products
  for i in products:
    try:
        p.update({i[0].strip(): float(i[1].strip())*q[i[0].strip()]})    
    except:
        p[i[0].strip()] = 0
  # p = {'I1': 70, 'I2': 160, 'I3': 140, 'I4': 60, 'I5': 20, 'I6': 0}
  return round(sum(p.values()),1)

def req4(transactions, products):
  q = {}
  p = {}
  g = []
  total = 0
  #get numbers of pro
  for i in transactions:
    for j in i[1]:
        try:
          q.update({j: q[j]+1})    
        except:
          q[j] = 1
  # Ex: q = {'I1': 7, 'I2': 8, 'I5': 2, 'I4': 2, 'I3': 7}

  #get price of prod
  for i in products:
    try:
        p.update({i[0].strip(): int(i[1].strip())*q[i[0].strip()]})    
    except:
        p[i[0].strip()] = 0
  # p = {'I1': 70, 'I3': 160, 'I2': 160, 'I4': 60, 'I5': 20, 'I6': 0}
   
  rmax = p[max(p, key=p.get)]
  for i in p:
    if p[i] == rmax:
      g.append(i)
      
  return sortIndex(g)

def req5(history, k):
  u = []
  his = {}
  # get info u
  for i in history:
    his.update({i[0][0]: len([e for e in i[1]])})
  if k > len(his) or k <= 0:
    return u
  # Ex: his = {'U1': 2, 'U2': 3, 'U3': 3, 'U4': 1, 'U5': 1}


  his = sortDictByKey(his)

  # sort dict by value
  sorted_dict = sortDictByVal(his,True)

  # get top u
  for i in sorted_dict:
    u.append(i)
    k -=1
    if(k <= 0):
      break
  return u

def req6(transactions, history, k):
  imax = []
  user = user_total_trans(transactions, history)
  try:
    rmax = user[k][max(user[k], key=user[k].get)]
  except:
    return imax
  for i in user[k]:
    if user[k][i] == rmax:
      imax.append(i)
  imax = sortIndex(imax)
  return imax

def req7(transactions, history):
  imax = []
  dic_info = {}
  user = user_total_trans(transactions, history)
  xmin = min([ len(i[1]) for i in history])
  for i in history:
    if len(i[1]) == xmin:
      for j in user[i[0][0]]:
        try:
          dic_info.update({j: dic_info[j]+1})    
        except:
          dic_info[j] = 1
  dic_info = sortDictByVal(dic_info,True)
  xmin = max([dic_info[i] for i in dic_info])
  for i in dic_info:
    if dic_info[i] == xmin:
      imax.append(i)  
  return imax

def req8(transactions, history, k):
  val_max = 0
  lmax = []
  res = []
  user = user_total_trans(transactions, history)
  # if user has k
  try: 
    user[k]
  except KeyError:
    return res

  for u1 in user:
    if u1 == k:
      continue
    ul = []
    vl = []
    lkey = list(user[u1].keys()) + list(user[u1].keys())
    for i in lkey:
      try:
        u_val =  user[u1][i]
      except:
        u_val = 0
      try: 
        v_val = user[k][i]
      except:
        v_val = 0
      ul.append(u_val)
      vl.append(v_val)
    u = np.array(ul)
    v = np.array(vl)
    cs = sum(u*v)/(np.linalg.norm(u,2)*np.linalg.norm(v,2))
    lmax.append([u1,cs])
    val_max = max(val_max,cs)
  for i in lmax:
    if i[1] == val_max:
      res.append(i[0])
  return res

def req9(transactions, history, products):
  q = {}
  p = {}
  b = []

  #get numbers of pro
  for i in transactions:
    for j in i[1]:
        try:
          q.update({j: q[j]+1})    
        except:
          q[j] = 1
  
  #get pri of prod
  for i in products:
    try:
        p.update({i[0].strip(): int(i[1].strip())*q[i[0].strip()]})    
    except KeyError:
        p[i[0].strip()] = 0
  for i in p:
    if p[i] == 0:
      b.append(i)
  return b

def req10(history, transactions, products, k):
  user = user_total_trans(transactions, history)
  prod = {}
  rank = [0,0,0]
  for i in products:
    prod[i[0].strip()] = int(i[3].strip())

  try:
    for i in user[k]:
      rank[prod[i]-1]+= user[k][i]
  except:
    return None

  res = max(rank)
  for i in range(0,3):
    if rank[i] == res:
      return i+1
  return res
