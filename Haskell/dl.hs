


doubleList [] = []
doubleList (x : xs) = (2*x) : doubleList xs

funOnList f [] = []
funOnList f (x : xs) = (f x) : funOnList f xs 

myfun :: (Num a) => a -> a
myfun x = x*x

apa = (funOnList myfun [1,2,3])

main = putStrLn ( apa )

