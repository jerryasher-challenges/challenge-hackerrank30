(require 'clojure.string)

(let [ignore (read-line) 
      data (read-line)
      arr (clojure.string/split data #"\s+")
      rarr (reverse arr)
      line (clojure.string/join " " rarr)]
  (println line))

