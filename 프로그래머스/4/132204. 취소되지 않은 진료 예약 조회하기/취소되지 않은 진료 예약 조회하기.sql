# 2022년 4월 13일 취소되지 않은 CS 진료 예약 내역을 조회
# 진료 예약 번호, 환자 이름, 환자 번호, 진료과 코드, 의사 이름, 진료 예약 일시
SELECT
    A.APNT_NO, P.PT_NAME, P.PT_NO, D.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM 
    (SELECT 
        APNT_YMD, APNT_NO, PT_NO, MDDR_ID 
    FROM 
        APPOINTMENT
    WHERE 
        MCDP_CD = 'CS'
        AND APNT_CNCL_YN = 'N'
        AND DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = '2022-04-13'
    ) AS A
    JOIN PATIENT AS P
        ON P.PT_NO = A.PT_NO
    JOIN DOCTOR AS D
        ON D.DR_ID = A.MDDR_ID
ORDER BY 
    A.APNT_YMD;