(use '[clojure.string :only (split triml)])

(let [N_t (read-line) 
      N (Integer/parseInt N_t)]
  (doseq [i (range 1 11)]
    (println (str N " x " i " = " (* N i)))))

