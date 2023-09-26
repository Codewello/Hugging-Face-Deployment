<script>
  import axios from "axios";

  //current vars
  let emotion = "";
  let response = [];
  let loading =false;

  //handle sending the api to huggingface
  const handleSend = async (e) => {
    e.preventDefault();

    loading=true;
   
      const space = await axios.post(
        "https://hossameldin-emo-roberta.hf.space/run/predict",
        { data: [emotion] },
        {
          headers: {
            Authorization: "Bearer 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",
            "Content-Type": "application/json",
          },
        }
      );
      console.log(space);
      response = space.data.data;
      loading= false;
      emotion = "";

    
  };

  //function to handle the text changed
  const handleText = (e) => {
    e.preventDefault();
    emotion = e.target.value = e.target.value.replace(/x/g, "");
  };
</script>

<div class="main">
  <div>
    <p>
      {#if response.length > 0}
        <div>
          <p>{`Emotion : ${response[0]}`}</p>
          <p>{`Score : ${response[1]}`}</p>
        </div>
      
      {/if}
    </p>
    <textarea value={emotion} on:change={handleText} class="text-input" />
  </div>
  <div>
    <button on:click={handleSend} class="send">
      {#if loading === true }
          Loading.....
      {:else}
         Send
      {/if}
    
    </button>
  </div>
</div>

<style>
  .main {
    width: 700px;
  }
  .text-input {
    width: 100%;
    padding: 25px;
    border-radius: 10px;
    margin-bottom: 30px;
  }

  .send {
    width: 250px;
  }
</style>
