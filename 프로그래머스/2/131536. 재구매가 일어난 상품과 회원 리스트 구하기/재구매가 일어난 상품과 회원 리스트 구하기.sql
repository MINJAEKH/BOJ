-- 코드를 입력하세요
# 동일한 회원이 동일한 상품을 재구매한 데이터
# 재구매한 회원 아이디와 구매한 상품 아이디 출력
# 회원 아이디 기준 오름차순, 상품 아이디 기준 내림차순
SELECT USER_ID, PRODUCT_ID # , COUNT(PRODUCT_ID)
FROM ONLINE_SALE AS S1
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(PRODUCT_ID) >= 2
ORDER BY USER_ID, PRODUCT_ID DESC;