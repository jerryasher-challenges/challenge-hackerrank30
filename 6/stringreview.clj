(require 'clojure.string)

(let [N_t (read-line) 
      N (Integer/parseInt N_t)]
  (doseq [i (range N)]
    (let [line (read-line) 
          first (take-nth 2 line)
          second (take-nth 2 (rest line))]
      (println (clojure.string/join
                [(clojure.string/join first) 
                 \space
                 (clojure.string/join second)])))))


