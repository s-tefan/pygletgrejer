

prepend x y = x : y

prutt :: IO()
prutt = do { let a = [1] in print (prepend 2 a)}

fak :: Int -> Int
fak 0 = 1
fak n = n * fak (n-1)


blaha _ = "annat"
-- blaha (_:_) = "lista"


lång :: (RealFloat a) => a -> String
lång längd
    | längd < 160 = "Rätt kort"
    | längd < 170 = "Halvkort"
    | längd < 190 = "Medellång"
    | otherwise = "Rätt lång"


plutt a = print a

data Shape = Circle Float Float Float 
    | Rectangle Float Float Float Float
    | Triangle Float Float Float Float Float Float 
-- Circle cx cy r | Rectangle ulx uly lrx lry

area (Circle _ _ r) = pi*r^2
area (Rectangle ulx uly lrx lry) = (abs $ lrx-ulx)*(abs $ uly-lry)
area (Triangle x1 y1 x2 y2 x3 y3) = abs $ ( (x3-x1)*(y2-y1) - (x2-x1)*(y3-y1) )/2





apa :: String -> String
apa _ = "bla"

-- apa :: (Num a) => a -> String
-- apa Num _ = "bu"


-- Hur gör man sånt här?
data Kort = Hjärter | Spader | Ruter | Klöver

(+++) :: Kort -> Kort -> Kort
(+++) Hjärter Spader = Ruter






main = print (fak 5)