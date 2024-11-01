-- 코드를 입력하세요
SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, D.MCDP_CD, D.DR_NAME, A.APNT_YMD 
FROM APPOINTMENT AS A
LEFT JOIN PATIENT AS P ON A.PT_NO = P.PT_NO
LEFT JOIN DOCTOR AS D ON A.MDDR_ID = D.DR_ID
WHERE DATE_FORMAT(A.APNT_YMD, '%m') = '04' AND DATE_FORMAT(A.APNT_YMD, '%d') = '13' AND A.APNT_CNCL_YN = 'N' AND D.MCDP_CD = 'CS'
ORDER BY A.APNT_YMD

