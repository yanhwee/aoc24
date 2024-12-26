import Control.Applicative (liftA2)
import Data.List (inits, tails)

main :: IO ()
main = getContents >>= (print . solution)

solution :: String -> Int
solution = solve . parse

parse :: String -> [[Int]]
parse = map (map read . words) . lines

solve :: [[Int]] -> Int
solve = length . filter isActuallySafe

pairwise :: [a] -> [(a,a)]
pairwise = zip <*> tail

isMonotone :: [Int] -> Bool
isMonotone = liftA2 (||) (monotone (<=)) (monotone (>=))
    where monotone f = all (uncurry f) . pairwise

isGradual :: [Int] -> Bool
isGradual = all (uncurry gradual) . pairwise
    where gradual = ((withinRange . abs) .) . subtract
          withinRange = liftA2 (&&) (>= 1) (<= 3)

removeLevels :: [Int] -> [[Int]]
removeLevels = liftA2 (zipWith (++)) inits (tail . tails)

isSafe :: [Int] -> Bool
isSafe = liftA2 (&&) isMonotone isGradual

isActuallySafe :: [Int] -> Bool
isActuallySafe = any isSafe . removeLevels