-- 자동차 종류가 트럭
-- 대역 기록별로 대여 금액(FEE)를 구해 대여 기록 ID와 금액 리스트 출력
-- 대여 금액 기준 내림차순 정렬 > 대여 기록 ID 기준 내림차순 정렬

SELECT 
    R.HISTORY_ID,
    ROUND(R.DAILY_FEE*R.PERIOD*(1-IFNULL(P.DISCOUNT_RATE, 0)/100),0) AS FEE
FROM 
    (
        SELECT 
            C.CAR_TYPE, C.DAILY_FEE, H.HISTORY_ID,
            DATEDIFF(H.END_DATE, H.START_DATE) + 1 AS PERIOD,
            CASE
                WHEN DATEDIFF(END_DATE, START_DATE)+1 >= 90 THEN '90일 이상'
                WHEN DATEDIFF(END_DATE, START_DATE)+1 >= 30 THEN '30일 이상'
                WHEN DATEDIFF(END_DATE, START_DATE)+1 >= 7 THEN '7일 이상'
            END AS DURATION_TYPE            
        FROM
            (
                SELECT CAR_ID, CAR_TYPE, DAILY_FEE
                FROM CAR_RENTAL_COMPANY_CAR 
                WHERE CAR_TYPE = '트럭'
            ) AS C
            JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
            ON C.CAR_ID = H.CAR_ID                
    ) AS R
    LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P
    ON R.CAR_TYPE = P.CAR_TYPE AND R.DURATION_TYPE = P.DURATION_TYPE
ORDER BY FEE DESC, R.HISTORY_ID DESC;
