from transformers import pipeline
import gradio as gr


def classify(text):
    pipe = pipeline("text-classification",
                    model="SamLowe/roberta-base-go_emotions")

    results = pipe(text)[0]
    score = float(results['score'])
    # Format the score with 5 decimal places
    score_formatted = "{:.5f}".format(score)
    return results['label'], score_formatted


inf = gr.Interface(
    
    inputs=gr.Text(),
    outputs=[gr.Text(label='Type'), gr.Number(label='Score')],
    fn=classify,
    title="deployment on huggginface"
)
#inf.launch()
inf.launch(auth=('user','password'),auth_message="Enter User & Password ")

