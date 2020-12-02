data VonN = Noll | Kuken | Eftr VonN deriving(Show)

toVonN 0 = Noll
toVonN n
  | n > 0 = Eftr (toVonN (n-1))
  | otherwise = Kuken

fromVonN Noll = 0
fromVonN (Eftr n) = fromVonN n + 1

fore :: VonN -> VonN
fore Noll = Kuken
fore (Eftr n) = n

vnplus :: VonN -> VonN -> VonN
vnplus n Noll = n
vnplus n (Eftr m) = vnplus (Eftr n) m

vnminus :: VonN -> VonN -> VonN
vnminus n Noll = n
vnminus Noll n = Kuken
vnminus (Eftr n) (Eftr m) = vnminus n m 
