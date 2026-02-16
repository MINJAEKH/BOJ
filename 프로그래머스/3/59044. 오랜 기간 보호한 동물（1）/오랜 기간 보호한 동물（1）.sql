-- 코드를 입력하세요
# 동물보호소에 들어온 동물 정보 INS
# 입양 보낸 동물 정보 OUTS
# 입양을 못간 동물 중 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일 조회
# 보호 시작일 오름차순
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS AS I LEFT JOIN ANIMAL_OUTS AS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY I.DATETIME
LIMIT 3;