(use '[clojure.string :only (split triml)])

(let [N_t (read-line) 
      N (Integer/parseInt N_t)
      is_odd (= 1 (mod N 2))
      ]
  (println (cond is_odd "Weird"
                 (<= N 5) "Not Weird"
                 (<= N 20) "Weird"
                 :else "Not Weird")))
