/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
/*
 * Materia:
 * Programacion Inteligente
 * Participantes:
 * Dante Alejandro Alegria Romero
 * Andrea Margarita Balandran Felix
 * Metodo:
 * Metodo de Gauss Jordan
 * Descripcion:
 * El metodo de Gauss Jordan es un metodo de resolucion de sistemas de ecuaciones lineales
 * que se basa en la idea de convertir la matriz aumentada en la matriz identidad
 * para asi poder obtener la solucion del sistema, esto se logra mediante la eliminacion
 * de incognitas, es decir, se hace cero a todos los elementos de la columna que no sean el pivote
 * y se convierte en 1 al pivote, para asi poder obtener la solucion del sistema
 * Fecha de la ultima modificacion:
 * 21/04/2023
 */

import java.awt.Desktop;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import javax.swing.ImageIcon;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author Dante Alegria
 */
public class Proeye extends javax.swing.JFrame {

    int f, c;// variables usadas para almacenar las imensiones de la matriz aumentada

    DefaultTableModel modelo = new DefaultTableModel();
    Boolean ban = false;

    public Proeye() {
        initComponents();

        this.setLocationRelativeTo(null);// al momento de ejecutar la aplicacion lo ventana se  centra en la pantalla
    }

    /**
     * @param m almacena los coeficientes de la matriz aumentada
     * @param r almaena los valores de la solucion de acda expresion
     * @return
     */
    public double[] cargarMatriz(double m[][], double r[]) {

        // recuerde que el metodo de Gauss Jordan trabaja con la idea de convertir la matriz aumentada en la matriz identidad
        for (int i = 0; i <= r.length - 1; i++) {
            double d, c = 0;
            d = m[i][i];// seleccionamos el pivote
            area_de_texto.append(Double.toString(d / 2) + "*fila" + (i + 1) + "\n");// muesra en el area de texto el pivote seleccionado
            for (int s = 0; s <= r.length - 1; s++) {// pasamos a convertir en 1 al pivote seleionado
                m[i][s] = ((m[i][s]) / d);
            }
            r[i] = ((r[i]) / d);

            // paso a mostrar las opraciones realizadas en la matriz aumentada
            for (int j = 0; j < r.length; j++) {

                for (int k = 0; k < r.length; k++) {
                    area_de_texto.append(Double.toString(m[j][k]) + "\t");
                }
                area_de_texto.append("|\t" + Double.toString(r[j]) + "\n");
            }
            area_de_texto.append("\n\n");// fin paso a motrar las opraciones realizadas en la matriz aumentada

            for (int x = 0; x <= r.length - 1; x++) {
                if (i != x) {
                    c = m[x][i];
                    area_de_texto.append("-" + Double.toString(c) + " * fila" + (i + 1) + "+ fila" + (x + 1) + "\n");// mustra en pantalla las opraciones que se realizaran por fila
                    for (int y = 0; y <= r.length - 1; y++) {// se hace cero a todos los elemntos de la colunma que no sean el pivote
                        m[x][y] = m[x][y] - c * m[i][y];

                    }
                    r[x] = r[x] - c * r[i];

                    // paso a mostrar las opraciones realizadas en la matriz aumentada
                    for (int j = 0; j < r.length; j++) {

                        for (int k = 0; k < r.length; k++) {
                            area_de_texto.append(Double.toString(m[j][k]) + "\t");
                        }
                        area_de_texto.append("|\t" + Double.toString(r[j]) + "\n");
                    }
                    area_de_texto.append("\n\n");// fin paso a motrar las opraciones realizadas en la matriz aumentada

                }// fin if (i != x)
            }// fin for (int x = 0; x <= r.length - 1; x++)

        }//fin bucle i
        return r;// retorna la solucion l sistema

    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">                          
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jLabel3 = new javax.swing.JLabel();
        fila = new javax.swing.JTextField();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTable1 = new javax.swing.JTable();
        jButtoncargar_matriz1 = new javax.swing.JButton();
        jPanel2 = new javax.swing.JPanel();
        jScrollPane2 = new javax.swing.JScrollPane();
        area_de_texto = new javax.swing.JTextArea();
        jLabel1 = new javax.swing.JLabel();
        jButtoncargar_matriz2 = new javax.swing.JButton();
        jLabel7 = new javax.swing.JLabel();
        jButtoncargar_matriz = new javax.swing.JButton();
        jSeparator1 = new javax.swing.JSeparator();
        jButton1 = new javax.swing.JButton();
        fila2 = new javax.swing.JTextField();
        intercambiar = new javax.swing.JButton();
        cantidad = new javax.swing.JTextField();
        fila11 = new javax.swing.JTextField();
        jLabel2 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        Columna = new javax.swing.JTextField();
        jLabel8 = new javax.swing.JLabel();
        jButton3 = new javax.swing.JButton();
        cantidad1 = new javax.swing.JTextField();
        escala = new javax.swing.JButton();
        filaNueva = new javax.swing.JTextField();
        fila4 = new javax.swing.JTextField();
        fila1 = new javax.swing.JTextField();
        fila33 = new javax.swing.JTextField();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        jLabel9 = new javax.swing.JLabel();
        jLabel10 = new javax.swing.JLabel();
        jLabel11 = new javax.swing.JLabel();
        jLabel12 = new javax.swing.JLabel();
        jLabel13 = new javax.swing.JLabel();
        jMenuBar1 = new javax.swing.JMenuBar();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jPanel1.setBackground(new java.awt.Color(153, 153, 153));
        jPanel1.setBorder(javax.swing.BorderFactory.createTitledBorder("Solución de Matrices By Dante Alegria"));
        jPanel1.setLayout(null);

        jLabel3.setFont(new java.awt.Font("Matura MT Script Capitals", 0, 36)); // NOI18N
        jPanel1.add(jLabel3);
        jLabel3.setBounds(180, 0, 610, 40);

        fila.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 1, true));
        fila.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                filaActionPerformed(evt);
            }
        });
        jPanel1.add(fila);
        fila.setBounds(310, 90, 80, 30);

        jTable1.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 1, true));
        jTable1.setFont(new java.awt.Font("Comic Sans MS", 0, 14)); // NOI18N
        jTable1.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {

            },
            new String [] {
                "x"
            }
        ));
        jScrollPane1.setViewportView(jTable1);

        jPanel1.add(jScrollPane1);
        jScrollPane1.setBounds(10, 170, 470, 200);

        jButtoncargar_matriz1.setFont(new java.awt.Font("Consolas", 0, 13)); // NOI18N
        jButtoncargar_matriz1.setText("Resolver Matriz");
        jButtoncargar_matriz1.setActionCommand("Resolver matriz");
        jButtoncargar_matriz1.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 1, true));
        jButtoncargar_matriz1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtoncargar_matriz1ActionPerformed(evt);
            }
        });
        jPanel1.add(jButtoncargar_matriz1);
        jButtoncargar_matriz1.setBounds(20, 380, 190, 30);

        jPanel2.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 2, true));

        area_de_texto.setEditable(false);
        area_de_texto.setColumns(20);
        area_de_texto.setRows(5);
        jScrollPane2.setViewportView(area_de_texto);

        jLabel1.setFont(new java.awt.Font("Shruti", 0, 14)); // NOI18N
        jLabel1.setText("Solución");

        jButtoncargar_matriz2.setFont(new java.awt.Font("Consolas", 0, 13)); // NOI18N
        jButtoncargar_matriz2.setText("Borrar");
        jButtoncargar_matriz2.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 1, true));
        jButtoncargar_matriz2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtoncargar_matriz2ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2.setLayout(jPanel2Layout);
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jScrollPane2)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel2Layout.createSequentialGroup()
                .addContainerGap(166, Short.MAX_VALUE)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel2Layout.createSequentialGroup()
                        .addComponent(jButtoncargar_matriz2, javax.swing.GroupLayout.PREFERRED_SIZE, 190, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(150, 150, 150))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel2Layout.createSequentialGroup()
                        .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(157, 157, 157))))
        );
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel2Layout.createSequentialGroup()
                .addGap(12, 12, 12)
                .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 18, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, 273, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 55, Short.MAX_VALUE)
                .addComponent(jButtoncargar_matriz2, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE))
        );

        jPanel1.add(jPanel2);
        jPanel2.setBounds(490, 20, 510, 410);

        jLabel7.setFont(new java.awt.Font("Shruti", 0, 14)); // NOI18N
        jLabel7.setText("Filas");
        jPanel1.add(jLabel7);
        jLabel7.setBounds(80, 40, 230, 50);

        jButtoncargar_matriz.setFont(new java.awt.Font("Consolas", 0, 13)); // NOI18N
        jButtoncargar_matriz.setText("Diseñar Matriz");
        jButtoncargar_matriz.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 1, true));
        jButtoncargar_matriz.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtoncargar_matrizActionPerformed(evt);
            }
        });
        jPanel1.add(jButtoncargar_matriz);
        jButtoncargar_matriz.setBounds(130, 130, 190, 30);
        jPanel1.add(jSeparator1);
        jSeparator1.setBounds(10, 120, 970, 3);

        jButton1.setFont(new java.awt.Font("Consolas", 0, 13)); // NOI18N
        jButton1.setText("Salir");
        jButton1.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });
        jPanel1.add(jButton1);
        jButton1.setBounds(230, 380, 100, 40);
        jPanel1.add(fila2);
        fila2.setBounds(80, 510, 130, 22);

        intercambiar.setText("Intercambiar");
        intercambiar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                intercambiarActionPerformed(evt);
            }
        });
        jPanel1.add(intercambiar);
        intercambiar.setBounds(250, 540, 130, 23);
        jPanel1.add(cantidad);
        cantidad.setBounds(420, 500, 130, 22);
        jPanel1.add(fila11);
        fila11.setBounds(250, 500, 130, 22);

        jLabel2.setText("Fila 2:");
        jPanel1.add(jLabel2);
        jLabel2.setBounds(250, 480, 40, 16);

        jLabel4.setText("sumar a");
        jPanel1.add(jLabel4);
        jLabel4.setBounds(20, 510, 50, 16);

        Columna.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 1, true));
        Columna.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ColumnaActionPerformed(evt);
            }
        });
        jPanel1.add(Columna);
        Columna.setBounds(60, 90, 80, 30);

        jLabel8.setFont(new java.awt.Font("Shruti", 0, 14)); // NOI18N
        jLabel8.setText("Columnas");
        jPanel1.add(jLabel8);
        jLabel8.setBounds(330, 40, 230, 50);

        jButton3.setText("Modificar");
        jButton3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton3ActionPerformed(evt);
            }
        });
        jPanel1.add(jButton3);
        jButton3.setBounds(20, 540, 190, 23);
        jPanel1.add(cantidad1);
        cantidad1.setBounds(20, 450, 120, 22);

        escala.setText("Escalar");
        escala.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                escalaActionPerformed(evt);
            }
        });
        jPanel1.add(escala);
        escala.setBounds(420, 540, 130, 23);
        jPanel1.add(filaNueva);
        filaNueva.setBounds(420, 450, 130, 22);
        jPanel1.add(fila4);
        fila4.setBounds(250, 500, 130, 22);
        jPanel1.add(fila1);
        fila1.setBounds(20, 480, 190, 22);
        jPanel1.add(fila33);
        fila33.setBounds(250, 450, 130, 22);

        jLabel5.setText("por");
        jPanel1.add(jLabel5);
        jLabel5.setBounds(160, 450, 40, 16);

        jLabel6.setText("Fila a multiplicar");
        jPanel1.add(jLabel6);
        jLabel6.setBounds(420, 430, 110, 16);

        jLabel9.setText("no funcionara, agregue las columnas restantes con 0");
        jPanel1.add(jLabel9);
        jLabel9.setBounds(590, 510, 390, 60);

        jLabel10.setText("Escalar");
        jPanel1.add(jLabel10);
        jLabel10.setBounds(420, 480, 40, 16);

        jLabel11.setText("Fila 1:");
        jPanel1.add(jLabel11);
        jLabel11.setBounds(250, 430, 40, 16);

        jLabel12.setText("Avisos: para ingresar las filas/columnas hay que iniciar por el 0     ");
        jPanel1.add(jLabel12);
        jLabel12.setBounds(590, 450, 390, 60);

        jLabel13.setText("Si la cantidad de filas es mayor a la de columnas, la resolucion automatica");
        jPanel1.add(jLabel13);
        jLabel13.setBounds(590, 490, 390, 60);

        setJMenuBar(jMenuBar1);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, 1009, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, 599, Short.MAX_VALUE)
                .addContainerGap())
        );

        jPanel1.getAccessibleContext().setAccessibleName("Solución de Matrices ");

        pack();
    }// </editor-fold>                        

    private void jButtoncargar_matrizActionPerformed(java.awt.event.ActionEvent evt) {                                                     
        /*
        * pasamos a mostrar los cuadros para llenar la matriz aumentada en la pantalla
         */

 /*
        * ejemplo si el sistema tiene 2 incognitas aparecera en la pantalla una matriz de 2x3
         */
        try {
            /*
            * ejemplo si el sistema tiene 2 incognitas aparecera en la pantalla una matriz de 2x3
             */
            f = Integer.parseInt(Columna.getText());
            c = Integer.parseInt(fila.getText());
           
            Object col[] = new Object[c];//  al erreglo mostrara en el titulo del JTabel las las incognitas y su solucion de la ecuaciom
            // ejemplo si el sistema tiene 2 incognitas aparecera en la pantalla una matriz de 2x3
            // se motrara en el titulo del JTable  x1  x2   d
            for (int j = 0; j < c; j++) {
                if (j < c - 1) {
                    col[j] = "X" + (j + 1);
                } else {
                    col[j] = "d";
                }
            }
            modelo = new DefaultTableModel(col, f);// se muestra el titulo y el Jtablet toma la dimension de la matriz aumentada
            jTable1.setModel(modelo);// el Jtablet toma la dimension de la matriz aumentada

        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "INGRESO ERRONEO", "MENSAJE", JOptionPane.PLAIN_MESSAGE);
        }
    }                                                    

    private void jButtoncargar_matriz2ActionPerformed(java.awt.event.ActionEvent evt) {                                                      
        // TODO add your handling code here:
        area_de_texto.setText("");
    }                                                     

    private void jButtoncargar_matriz1ActionPerformed(java.awt.event.ActionEvent evt) {                                                      
        /*
        * acontinuacion pasamos a gargar los datos ingresados en los cuadros del Jtablet en la matriz aumntada
         */
        try {

            int n = Integer.parseInt(Columna.getText());// alamacena el nuemro de ingonitas ingresado por teclado

            double m[][] = new double[n][n];// almacena los coeficientes de la matriz aumentada
            double r[] = new double[n];// almacena al valor de la solucion de cada ecuacion ejemplo si 2x+4x2=3 entonces debera ingresar el los cuadors  2   4   3   en donde , m[0][1]=2,m[0][2]=4  y   r[0]=3

            for (int i = 0; i < n; i++) {// pasamos a alamcenar en un arreglo los datos ingresados en el JTable
                for (int j = 0; j < n; j++) {//
                    m[i][j] = Double.parseDouble(String.valueOf(jTable1.getValueAt(i, j)));
                }
                r[i] = Double.parseDouble(String.valueOf(jTable1.getValueAt(i, n)));
            }

            double solucion[] = new double[n];// almacena la soluciones del sistema
            r = this.cargarMatriz(m, r);// llamada al metodo a calcula la solucion del sistema de eciones

            //pasamos a mostrar las soluciones del sistema en el area de texto
            for (int i = 0; i < n; i++) {
                area_de_texto.append("x" + (i + 1) + " = " + r[i] + "\n");
            }

        }//fin try
        catch (Exception e) {
            JOptionPane.showMessageDialog(null, "error ingreso de datos \n"
                    + "NOTA: verifique que no haya casillas seleccionadas ni vacias\n"
                    + " también verifique que el ingreso de tados sea correctos");
        }
    }                                                     

    private void filaActionPerformed(java.awt.event.ActionEvent evt) {                                     
        // TODO add your handling code here:
    }                                    

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {                                         
        // TODO add your handling code here:
        System.exit(0);
    }                                        
//boton para intercambiar filas
    private void intercambiarActionPerformed(java.awt.event.ActionEvent evt) {                                             
        // TODO add your handling code here:
         //intecarmbiamos la fila seleccionada con la fila que se encuentra en la posicion de la fila seleccionada
        int fila_1 = Integer.parseInt(fila11.getText());
        int fila_2 = Integer.parseInt(fila33.getText());

        for (int i = 0; i < c; i++) {
            double valor = Double.parseDouble(String.valueOf(jTable1.getValueAt(fila_1, i)));
            double valor2 = Double.parseDouble(String.valueOf(jTable1.getValueAt(fila_2, i)));
            jTable1.setValueAt(valor2, fila_1, i);
            jTable1.setValueAt(valor, fila_2, i);
        }
    }                                            

    private void ColumnaActionPerformed(java.awt.event.ActionEvent evt) {                                        
        // TODO add your handling code here:
    }                                       
//boton para modificar o ir resolviendo la matriz
    private void jButton3ActionPerformed(java.awt.event.ActionEvent evt) {                                         
        // TODO add your handling code here:
                // TODO add your handling code here:
          //inicializamos resultado
          double resultado = 0;
          //tomamos el valor del jtextfield cantidad
          String fraccion = cantidad1.getText();
          //si encuentra / en la cadena lo dividimos
          if (fraccion.contains("/")) {
              String[] partes = fraccion.split("/");
              //convertimos los valores a double
              double numerador = Double.parseDouble(partes[0]);
              double denominador = Double.parseDouble(partes[1]);
              //calculamos el resultado
               resultado = numerador / denominador;
              //mostramos el resultado
              
          } else {
              //si no encuentra / en la cadena mostramos un mensaje de error
               resultado = Integer.parseInt(cantidad1.getText());   
          }
          //tomamos el valor del jtextfield fila1
          int f1 = Integer.parseInt(fila1.getText());
          //tomamos el valor del jtextfield fila2
          int f2 = Integer.parseInt(fila2.getText());
          
          int cock = jTable1.getColumnCount();
          //multiplicamos resultado por la fila 1 y se lo agregamos a la fila 2
          //esto para todas las posiciones de la fila 2
          for (int i = 0; i < cock; i++) {
              double valor = Double.parseDouble(String.valueOf(jTable1.getValueAt(f2, i)));
              valor = valor + (resultado * Double.parseDouble(String.valueOf(jTable1.getValueAt(f1, i))));
              //mostramos la tabla modificada en el jtable
              jTable1.setValueAt(valor, f2, i);
          }
  
  
    }                                        

//Boton para escalar
    private void escalaActionPerformed(java.awt.event.ActionEvent evt) {                                       
        // TODO add your handling code here:
        // TODO add your handling code here:
        int fila_1 = Integer.parseInt(filaNueva.getText());
        int fila_2 = Integer.parseInt(filaNueva.getText());
       //tomamos el valor del jtextfield escala  
       double escalonar = Double.parseDouble(cantidad.getText());
        //separamos la cadena por el caracter /
        if (filaNueva.getText() != null)
        {
            for (int j = 0; j < c; j++) {
                double valor = Double.parseDouble(String.valueOf(jTable1.getValueAt(fila_1, j)));
                valor = valor * escalonar;
                jTable1.setValueAt(valor, fila_1, j);
            }
        }
        
    }                                      

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Proeye.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Proeye.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Proeye.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Proeye.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Proeye().setVisible(true);
            }
        });
    }
    // Variables declaration - do not modify                     
    private javax.swing.JTextField Columna;
    private javax.swing.JTextArea area_de_texto;
    private javax.swing.JTextField cantidad;
    private javax.swing.JTextField cantidad1;
    private javax.swing.JButton escala;
    private javax.swing.JTextField fila;
    private javax.swing.JTextField fila1;
    private javax.swing.JTextField fila11;
    private javax.swing.JTextField fila2;
    private javax.swing.JTextField fila33;
    private javax.swing.JTextField fila4;
    private javax.swing.JTextField filaNueva;
    private javax.swing.JButton intercambiar;
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton3;
    private javax.swing.JButton jButtoncargar_matriz;
    private javax.swing.JButton jButtoncargar_matriz1;
    private javax.swing.JButton jButtoncargar_matriz2;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel12;
    private javax.swing.JLabel jLabel13;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JMenuBar jMenuBar1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JSeparator jSeparator1;
    private javax.swing.JTable jTable1;
    // End of variables declaration                   
}
