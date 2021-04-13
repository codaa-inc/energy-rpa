/**
 * 지역구분코드를 판단해 리턴하는 함수
 * Param : 선택된 시/도 text, 선택된 구/군 text
 * Return : 지역구분코드 (area_gb_cd)
 * */
function getAreaGbCd(sido, gugun) {
    let area_gb_cd = null;
    let area0 = ["서울", "인천", "대전", "광주", "대구", "울산", "부산", "세종특별자치시", "경기",
        "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주특별자치도"];
    for (let i in area0) {
        if (area0[i] == sido) {
            //////////////////////// 2 Depth : 경기,강원,충북,경북,경남 ////////////////////////
            if (i == 8 || i == 9 || i == 10 || i == 14 || i == 15) {
                // 구군 세부 구분 배열
                const gyunggi = ["연천군", "포천시", "가평군", "남양주시", "의정부시", "양주시", "동두천시", "파주시"];
                const gangwon = ["고성군", "속초시", "양양군", "강릉시", "동해시", "삼척시"];
                const chungbuk = ["제천시"];
                const gyungbuk1 = ["봉화군", '청송군']
                const gyungbuk2 = ["울진군", "영덕군", "포항시", "경주시", "청도군", "경산시"];
                const gyungnam = ["거창군", "함양군"];
                if (sido == 8) {
                    // 중부1(경기) : 경기도(연천, 포천, 가평, 남양주, 의정부, 양주, 동두천, 파주)
                    if (gyunggi.includes(gugun)) {
                        area_gb_cd = 1;
                        // 중부2(서울, 경기) : 경기도(연천, 포천, 가평, 남양주, 의정부, 양주, 동두천, 파주 제외)
                    } else {
                        area_gb_cd = 3;
                    }
                } else {
                    // 중부1 : 강원도(고성, 속초, 양양, 강릉, 동해, 삼척 제외), 충청북도(제천), 경상북도(봉화, 청송)
                    if (sido == 9 && !gangwon.includes(gugun) || sido == 10 && chungbuk.includes(gugun) || sido == 14 && gyungbuk1.includes(gugun)) {
                        area_gb_cd = 0;
                        // 남부 : 경상북도(울진, 영덕, 포항, 경주, 청도, 경산), 경상남도(거창, 함양 제외)
                    } else if (sido == 14 && gyungbuk2.includes(gugun) || sido == 15 && !gyungnam.includes(gugun)) {
                        area_gb_cd = 4;
                        // 중부2 : 강원도(고성, 속초, 양양, 강릉, 동해, 삼척), 충청북도(제천 제외), 경상북도(봉화, 청송, 울진, 영덕, 포항, 경주, 청도, 경산 제외), 경상남도(거창, 함양)
                    } else {
                        area_gb_cd = 2;
                    }
                }
            //////////////////////// 1 Depth : 경기,강원,충북,경북,경남 외 모든 지역 ////////////////////////
            } else {
                // 중부2 : 인천,대전,세종,충남,전북
                if (i == 1 || i == 2 || i == 7 || i == 11 || i == 12) {
                    area_gb_cd = 2;
                // 중부2(서울,경기) : 서울,경기
                } else if (i == 0 || i == 8) {
                    area_gb_cd = 3;
                // 남부 : 대구,전남
                } else if (i == 4 || i == 13) {
                    area_gb_cd = 4;
                // 남부(부산,광주,울산)
                } else if (i == 3 || i == 5 || i == 6) {
                    area_gb_cd = 5;
                // 제주
                } else if (i == 16) {
                    area_gb_cd = 6;
                }
            }
            return area_gb_cd;
        }
    }
};