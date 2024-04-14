def get_air_quality(fine_dust) :
  if 0 <= fine_dust <= 30 :
    return "좋음"
  elif fine_dust <= 30 :
    return "보통"
  elif fine_dust <= 150 :
    return "나쁨"
  else :
    return "매우나쁨"
  
print(get_air_quality(15))
print(get_air_quality(85))
