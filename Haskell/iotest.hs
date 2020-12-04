import System.IO( isEOF )


main :: IO()
main = do {line <- getLine; putStrLn line}


eternal :: IO (Maybe a)luxia
eternal = do line <- getLine

             if (not (line == "")) 
                then do 
                    putStrLn line 
                    eternal
                else return Nothing
            


