-- 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차 한정
-- 해당 기간동안의 월별 자동차ID 별 총 대여 횟수 (컬럼명: RECORDS) 출력
-- 월 기준 오름차순 정렬 > 자동차 ID 기준 내림차순 정렬
-- 특정 월의 총 대여 횟수가 0인 경우는 결과에서 제외
SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(CAR_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
WHERE 
    MONTH(START_DATE) BETWEEN 8 AND 10 
    AND CAR_ID IN (
                    SELECT CAR_ID 
                    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                    WHERE MONTH(START_DATE) BETWEEN 8 AND 10 
                    GROUP BY CAR_ID
                    HAVING COUNT(*) >= 5
                  )
GROUP BY CAR_ID, MONTH(START_DATE)
HAVING COUNT(CAR_ID) > 0
ORDER BY MONTH, CAR_ID DESC;