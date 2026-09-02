(defun diagnose-flu ()
  (let ((fever "")
        (cough "")
        (throat ""))

    (format t "Do you have fever? (yes/no): ")
    (finish-output)
    (setq fever (read-line))

    (format t "Do you have cough? (yes/no): ")
    (finish-output)
    (setq cough (read-line))

    (format t "Do you have sore throat? (yes/no): ")
    (finish-output)
    (setq throat (read-line))

    (if (and (string-equal fever "yes")
             (string-equal cough "yes")
             (string-equal throat "yes"))
        (format t "~%Diagnosis: You may have Flu.~%")
        (format t "~%Diagnosis: Flu not detected.~%"))))

(diagnose-flu)