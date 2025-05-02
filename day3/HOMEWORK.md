### 質問設計の観点と意図
演習と同等のものを使用

### RAGの実装方法と工夫点
演習と同等のものを使用

### 結果の分析と考察
得られた結果を分析にはLLM as Judgeの考えを元に全ての回答の組み合わせでA/Bテストを行い各回答のランキングを計算させた。使用したLLMは各回答を生成したModelと同じモデルを使用した。

回答群は演習のInference Time Scalingに関する質問の回答をそのまま使用した。演習ではRAGの改良ステップごとに合計6つの回答を生成ており、それぞれ順に#0,#2・・・#5とする。A/Bテストの総当たりの結果、
#### google/gemma-2-2b-jpn-itモデル
0,1,2,3,4,5の順で評価された。A/Bテストの結果をほぼほぼAと返し、適切な回答を返さない。
```
実験で得られたコードのOutput。
=== RANKING ===
1. Answer #0 (Wins: 5)
2. Answer #1 (Wins: 4)
3. Answer #2 (Wins: 2)
4. Answer #3 (Wins: 2)
5. Answer #4 (Wins: 2)
6. Answer #5 (Wins: 0)
```

#### meta-llama/Meta-Llama-3-8B-Instructモデル
#4,5,2,1,0,3の順で評価された。#3が低い理由がわからないが、おおむね、演習で改良したのと同じ降順になっている。
元のモデルでは、Inference Time Scalingに関する関する知識がないのに、適当な順位になっているのが面白い。
```
実験で得られたコードのOutput。
=== RANKING ===
1. Answer #4 (Wins: 5)
2. Answer #5 (Wins: 4)
3. Answer #2 (Wins: 3)
4. Answer #1 (Wins: 2)
5. Answer #0 (Wins: 1)
6. Answer #3 (Wins: 0)
```
### 発展的な改善案 (任意)
特になし