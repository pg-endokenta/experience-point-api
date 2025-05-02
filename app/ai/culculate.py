from openai import OpenAI
from app.core.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY,
)


def get_experience_point_by_text(text: str) -> int:
    """
    テキストを受け取り、経験値を算出する
    """

    prompt = f"""
    あなたは経験値を算出するプロです．
    以下の<text>の内容から適切な経験値を算出してください．
    基本的にはかかったであろう分数を予測し，それを基準にしてください．

    例は以下です．
    - 20ポイント: 20分間の読書
    - 5ポイント: ちょっとの運動
    - 100ポイント: ガッツリ勉強
    - 20ポイント: 部屋を片付けた

    出力は正の整数値としてください．
    出力をpythonでintにキャストするので余分な文字列は不要です．

    <text>
    {text}
    <text>
    """

    completion = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}]
    )

    try:
        point = int(completion.choices[0].message.content)
        if point == 0:
            # If the response is 0, return a default value
            print("why 0")
    except ValueError:
        # If the response is not a valid integer, return a default value
        point = 0
    return point
