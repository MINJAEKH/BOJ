-- 코드를 입력하세요
-- 서울에 위치한 식당 ID 기준으로 조인
-- SELECT 식당 ID, 식당 이름, 음식 종류, 즐겨찾기 수, 주소, 리뷰 평균 주소
-- 리뷰 평균 점수는 소수점 세 번째 자리에서 반올림, 내림차순 정렬 .> 즐겨찾기 내림차순
SELECT I.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO AS I JOIN REST_REVIEW AS R ON I.REST_ID = R.REST_ID
WHERE I.ADDRESS LIKE "서울%"
GROUP BY REST_ID
ORDER BY SCORE DESC, FAVORITES DESC;