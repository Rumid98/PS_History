-- 코드를 입력하세요
SELECT UB.WRITER_ID AS USER_ID, UU.NICKNAME, SUM(UB.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS UB
JOIN USED_GOODS_USER AS UU ON UB.WRITER_ID = UU.USER_ID
WHERE UB.STATUS = 'DONE'
GROUP BY UB.WRITER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES