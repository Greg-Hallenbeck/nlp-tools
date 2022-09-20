def pipeline(nlp, text,
        cols=['lower_', 'pos_', 'is_stop',
             'is_digit', 'is_punct', 'text', 'lemma_'],
        labelcol=None, textcol=None):
    
    if type(text) == str:
        doc = nlp(text)
    
        df = pd.DataFrame()
    
        for col in cols:
            df[col] = [getattr(token, col) for token in doc]
        
        return df
    else:
    
        df = None
        for i in range(len(text)):
            text_df = process(nlp, text.iloc[i][textcol])
            text_df[labelcol] = [text.iloc[i][labelcol]]*len(text_df)
            
            if (type(df) != None):
                df = pd.concat([df, text_df], axis=0)
            else:
                df = text_df
        
        cols.insert(0,labelcol)
        df = df[cols]
        
        return df
