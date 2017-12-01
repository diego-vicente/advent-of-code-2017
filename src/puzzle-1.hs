import Data.Char (digitToInt)
import Data.List (splitAt)

-- Solve the problem 1.1
captcha :: String -> Int
captcha str = solve $ (map digitToInt) (str ++ [str !! 0])
  where solve [] = 0
        solve (_:[]) = 0
        solve (y:x:xs) = if x == y then x + solve (x:xs)
                         else solve (x:xs)

-- Solve the problem 1.2
captcha' :: String -> Int
captcha' str = foldr (+) 0 $ zipWith (sumIf) half half'
  where (half, half') = splitAt ((length str) `div` 2) $ map digitToInt $ str
        sumIf a b = if a == b then a + b else 0
