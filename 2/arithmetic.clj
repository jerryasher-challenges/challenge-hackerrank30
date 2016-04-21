(def mealCost (Float/parseFloat (read-line))) ;; base meal cost
(def tipPercent (Integer/parseInt (read-line))) ;; tip percentage
(def taxPercent (Integer/parseInt (read-line))) ;; tax percentage

;; Write your calculation code here.
(def cost (* mealCost (+ 1 (/ (+ tipPercent taxPercent) 100.0))))

;; cast the result of the rounding operation to an int and save it as totalCost
(def totalCost (Math/round cost))

;; Print your result
(println (str "The total meal cost is " totalCost " dollars."))
