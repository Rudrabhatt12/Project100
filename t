import Data.List;

endsWithOneOf :: String -> [String] -> Bool
endsWithOneOf str ends = (or . map (\end -> end `isSuffixOf` str)) ends 

consonants :: [Char]
consonants = ['a'..'z'] \\ "aeiou"

pluralize :: String -> String
pluralize str
    | str `endsWithOneOf` (words "s x z ch sh" ++ (map (:"o") consonants)) = str ++ "es"
    | str `endsWithOneOf` (map (:"y") consonants) = init str ++ "ies"
    | str `endsWithOneOf` ["f"] = init str ++ "ves"
    | str `endsWithOneOf` ["fe"] = (init.init) str ++ "ves"
    | otherwise = str ++ "s"